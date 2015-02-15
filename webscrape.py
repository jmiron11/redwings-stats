import sqlite3
from datetime import datetime, date, time
import re
import requests
from bs4 import BeautifulSoup

# unformatted string is a date in the form "Day Month Day, Year"
def formatDate(unformatted):
	date = datetime.strptime(unformatted, "%a %b %d, %Y")
	date = date.strftime("%Y-%m-%d")
	return date


# get the soup for the website
schedule_html = "http://redwings.nhl.com/club/schedule.htm"
schedule_req = requests.get(schedule_html)
schedule_data = schedule_req.text
schedule_soup = BeautifulSoup(schedule_data)

# dates contains all of the days the detroit red wings play on
data = []

# access the schedule table from the schedule_html above and get elements
table_data = table = schedule_soup.find('table', class_='data', border='0', cellspacing='0', cellpadding='1')
for row in table.find_all("tr"):
	cells = row.find_all("td")
	cells = [element.text.strip() for element in cells]
	if len(cells) >= 5 and cells[0] != 'Date':
		data.append([element for element in cells if element])

# data now holds the table information
# format data into proper lists for the below insert into database

for list_ in data:
	while len(list_) < 6:
		list_.append(None)
	for index, ele in enumerate(list_):
		if index == 0:
			list_[index] = formatDate(ele)
		elif index == 4:
			if ele != None and len(ele.split()) >= 6:
				if "OT" in ele:
					list_[5] = "OT"
				elif "SO" in ele:
					list_[5] = "SO"
				else:
					list_[5] = "NONE"

				score = re.findall(r'\d+', ele)
				if (score[0] > score[1]):
					list_[4] = "A"
				else:
					list_[4] = "H"
			else:
				list_[4] = "NA"
				list_[5] = "NONE"

conn = sqlite3.connect('schedule.db')
c = conn.cursor()

#create a table command
# date will be in the form "YYYY:MM:DD"
# visitor will hold "(away team name)"
# home will hold "(home team)"
# time will hold time in form "H:MM (PM/AM)" in ET
# result will either hold H,A, or NA based on whether home/away has won, or NA if not played yet
# extra will hold whether it went to extra time, "NONE" , "OT", "SO" for respective cases
#c.execute('''CREATE TABLE schedule(date TEXT, visitor TEXT, home TEXT, time TEXT, result TEXT, extra TEXT)''')


#add information to the schedule database
for list_ in data:
	c.execute('INSERT INTO schedule VALUES (?,?,?,?,?,?)', list_)

conn.commit()
conn.close()






import sqlite3
import requests
from bs4 import BeautifulSoup

# get the soup for the website
schedule_html = "http://redwings.nhl.com/club/schedule.htm"
schedule_req = requests.get(schedule_html)
schedule_data = schedule_req.text
schedule_soup = BeautifulSoup(schedule_data)

# dates contains all of the days the detroit red wings play on
data = []

table_data = table = schedule_soup.find('table', class_='data', border='0', cellspacing='0', cellpadding='1')
for row in table.find_all("tr"):
	cells = row.find_all("td")
	cells = [element.text.strip() for element in cells]
	if len(cells) >= 5 and cells[0] != 'Date':
		data.append([element for element in cells if element])

# data now holds the table information

conn = sqlite3.connect('schedule.db')
c = conn.cursor()

#create a table command
#c.execute('''CREATE TABLE schedule(date text, visitor text, home text, time text, result text)''')

#add information to the table
for list_ in data:
	if len(list_) == 6:
		del list_[5:]
		c.execute('INSERT INTO schedule VALUES (?,?,?,?,?)', list_)
	elif len(list_) == 5:
		del list_[4:]
		list_.append(None)
		c.execute('INSERT INTO schedule VALUES (?,?,?,?,?)', list_)


conn.commit()
conn.close()









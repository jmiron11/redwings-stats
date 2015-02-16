import os.path
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
schedule_text = schedule_req.text
schedule_soup = BeautifulSoup(schedule_text)

# dates contains all of the days the detroit red wings play on
schedule_data = []

# access the schedule table from the schedule_html above and get elements
table = schedule_soup.find('table', class_='data', border='0', cellspacing='0', cellpadding='1')
for row in table.find_all("tr"):
	cells = row.find_all("td")
	cells = [element.text.strip() for element in cells]
	if len(cells) >= 5 and cells[0] != 'Date':
		schedule_data.append([element for element in cells if element])

# data now holds the table information
# format data into proper lists for the below insert into database

for list_ in schedule_data:
	while len(list_) < 6:
		list_.append(None)
	for index, ele in enumerate(list_): 
		if index == 0:									# the date is stored in index 0
			list_[index] = formatDate(ele)
		elif index == 4: 								# set up the fourth index a
			if ele != None and len(ele.split()) >= 6: 	# extend number of elements to 6 in each list
				if ") OT" in ele: 						# check for shootout, overtime, or neither
					list_[5] = "OT"
				elif ") SO" in ele:
					list_[5] = "SO"
				else:
					list_[5] = "NONE"

				score = re.findall(r'\d+', ele) 		# find the number score using regex
				if (len(score) != 2):
					list_[4] = "NA"
					list_[5] = "NONE"
				elif (score[0] > score[1]):
					list_[4] = "A" 						# store results as either home or away win
				else:
					list_[4] = "H"
			else:
				list_[4] = "NA"
				list_[5] = "NONE"
 
#schedule_data holds the red wings schedule information to be placed in schedule table
#team_game_data holds the red wings statistics per game to be placed in team_game table
#player_data holds the red wings player statistics current season statistics

conn = sqlite3.connect('redwings.db')  					# close the database
c = conn.cursor()

#create a table command
# date will be in the form "YYYY:MM:DD"
# visitor will hold "(away team name)"
# home will hold "(home team)"
# time will hold time in form "H:MM (PM/AM)" in ET
# result will either hold H,A, or NA based on whether home/away has won, or NA if not played yet
# extra will hold whether it went to extra time, "NONE" , "OT", "SO" for respective cases

# if not (os.path.isfile("./schedule.db")):
c.execute('CREATE TABLE IF NOT EXISTS schedule(date TEXT, visitor TEXT, home TEXT, time TEXT, result TEXT, extra TEXT)')
	#add information to the schedule database
for list_ in schedule_data :
	c.execute('INSERT INTO schedule VALUES (?,?,?,?,?,?)', list_)

	## add interface for replacing information and updating database whenever script is run.

conn.commit() 	# close the connection
conn.close()






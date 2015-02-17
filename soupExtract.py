from datetime import datetime, date, time
import re
import requests
from bs4 import BeautifulSoup


# formats the date, returns a string in form YYYY-MM-DD
# unformatted string is a date in the form "Day Month Day, Year"
def formatDate(unformatted):
	date = datetime.strptime(unformatted, "%a %b %d, %Y")
	date = date.strftime("%Y-%m-%d")
	return date

# returns the soup from an html address
def htmlToSoup(address):
	req = requests.get(address)
	text = req.text
	soup = BeautifulSoup(text)
	return soup

#returns a list of lists that holds schedule data
def schedule(soup):
	# dates contains all of the days the detroit red wings play on
	schedule_data = []

	# access the schedule table from the schedule_html above and get elements
	schedule_table = soup.find('table', class_='data', border='0', cellspacing='0', cellpadding='1')
	for row in schedule_table.find_all("tr"):
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

	return schedule_data

def seasonPlayerData(soup):
	season_player_data = []

	data_table = soup.find('table', class_='data', cellpadding='0', cellspacing='0')
	for row in data_table.find_all("tr"):
		cells = row.find_all("td")
		cells = [element.text for element in cells]
		if cells[0] != '#':
			season_player_data.append([element for element in cells if element])


	return season_player_data

# returns a list of lists that holds data from boxscores
def boxScoreData(soup):


def playerGameData(soup):
	# webscrape for the html's of boxscores and store in a list
	# store in list
	address_list = []

	data_table = soup.find_all('td', class_='leftAlignedColumn')
	data_table = [element.a.get('href') for element in data_table]
	address_list.append([element for element in data_table if element])
	
	# change recap to boxscore in each of the data_table elements
	address_list = address_list[0]
	for element in address_list:
		element = element.replace("recap", "boxscore") # THIS IS CURRENTLY NOT WORKING

	# address_list now holds all addresses webscrape those webpages for player game data
	for address in address_list:
		address_soup = htmltoSoup(address)
		address_data = # FUNCTION TO GET DATA FROM BOXSCORE

	return #SOME JUNK
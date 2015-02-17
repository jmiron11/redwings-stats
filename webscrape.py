import sqlite3
from datetime import datetime, date, time
from bs4 import BeautifulSoup

import soupExtract

schedule_soup = soupExtract.htmlToSoup("http://redwings.nhl.com/club/schedule.htm")
schedule_data = soupExtract.schedule(schedule_soup)

season_player_soup = soupExtract.htmlToSoup("http://redwings.nhl.com/club/stats.htm?season=20142015%20-%2014/15%20season%20player%20stats")
season_player_data = soupExtract.seasonPlayerData(season_player_soup)

prev_season_player_soup = soupExtract.htmlToSoup("http://redwings.nhl.com/club/stats.htm?season=20132014")
prev_season_player_data = soupExtract.seasonPlayerData(prev_season_player_soup)

player_game_soup = soupExtract.htmlToSoup("http://redwings.nhl.com/club/gamelog.htm")
player_game_data = soupExtract.playerGameData(player_game_soup)

# schedule_data holds the red wings schedule information to be placed in schedule table
# team_game_data holds the red wings statistics per game to be placed in team_game table
# player_data holds the red wings player statistics current season statistics

for list_ in player_game_data:
	print(list_)

# conn = sqlite3.connect('redwings.db')  					# close the database
# c = conn.cursor()

# # create a table command
# # date will be in the form "YYYY:MM:DD"
# # visitor will hold "(away team name)"
# # home will hold "(home team)"
# # time will hold time in form "H:MM (PM/AM)" in ET
# # result will either hold H,A, or NA based on whether home/away has won, or NA if not played yet
# # extra will hold whether it went to extra time, "NONE" , "OT", "SO" for respective cases

# # if not (os.path.isfile("./schedule.db")):
# c.execute('CREATE TABLE IF NOT EXISTS schedule(date TEXT, visitor TEXT, home TEXT, time TEXT, result TEXT, extra TEXT)')
# for list_ in schedule_data :
# 	c.execute('INSERT OR REPLACE INTO schedule VALUES (?,?,?,?,?,?)', list_)

# c.execute('CREATE TABLE IF NOT EXISTS season_player_stats(num INTEGER, pos TEXT, name TEXT, gp INTEGER, g INTEGER, a INTEGER, p INTEGER, plusminus INTEGER, pim INTEGER, pp INTEGER, sh INTEGER, gw INTEGER, s INTEGER, spercent INTEGER)')
# for list_ in season_player_data:
# 	c.execute('INSERT OR REPLACE INTO season_player_stats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', list_)

# c.execute('CREATE TABLE IF NOT EXISTS prev_season_player_stats(num INTEGER, pos TEXT, name TEXT, gp INTEGER, g INTEGER, a INTEGER, p INTEGER, plusminus INTEGER, pim INTEGER, pp INTEGER, sh INTEGER, gw INTEGER, s INTEGER, spercent INTEGER)')
# for list_ in prev_season_player_data:
# 	c.execute('INSERT OR IGNORE INTO prev_season_player_stats VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', list_)

# ## add interface for replacing information and updating database whenever script is run.

# conn.commit() 	# close the connection
# conn.close()






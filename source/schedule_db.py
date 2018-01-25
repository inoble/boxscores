import os, operator
import dbf

def schedule_db():

	# location of NBA Live 06 saved games
	target_dir = r'C:\Users\Ian\Documents\NBA Live 06\saves'
	
	# number of games in a season
	games = 1502

	# list to contain each directory within target_dir
	directory_list = []

	# add items to directory_list
	for d in os.listdir(target_dir):
		bd = os.path.join(target_dir, d)
		if os.path.isdir(bd): 
			directory_list.append(bd)

	# find most recently modified directory		
	latest_subdir = max((os.path.getmtime(f),f) for f in directory_list)[1]
	
	# point towards the most recently edited scheduleseason.dbf database	
	location = (latest_subdir + '\\' + 'scheduleseason.dbf')

	# assign most recently modified scheduleseason.dbf to the dbf module 
	schedule_database = dbf.Table(location)
		
	schedule_db = []

	# Convert season schedule to a list using dbf module	
	with schedule_database:
		
		index = schedule_database.create_index (lambda rec: (rec.id))
		
		date = 0
		
		for x in range(games):
		
			matches = index.search (match= (date,), partial=True)
						
			for item in matches:
			
				schedule_db.append([
								item[5],		# Date [0]
								item[6],		# Time [1]
								item[10],		# Home Team [2]
								item[11],		# Away Team [3]
								item[12],		# Home Score [4]
								item[13],		# Away Score [5]
								item[8],		# Played? [6]
								item[9],		# Overtime? [7]
								])
			
			date = date + 1
	
	# order the database of scheduled games first by whether the game was played, then by date
	schedule_db_sorted = sorted(schedule_db, key=operator.itemgetter(6, 0), reverse=True)
		
	return schedule_db_sorted
	
schedule_db()
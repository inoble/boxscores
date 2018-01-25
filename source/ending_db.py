import dbf, operator, os

def ending_db():

	# location of NBA Live 06 saved games
	target_dir = r'C:\Users\Ian\Documents\NBA Live 06\saves'

	# list to contain each directory within target_dir
	directory_list = []

	# add items to directory_list
	for d in os.listdir(target_dir):
		bd = os.path.join(target_dir, d)
		if os.path.isdir(bd): 
			directory_list.append([
								[bd],						# directory name
								[os.path.getmtime(bd)],		# time the directory was last modified
								])
	
	# sort in order of which directory was last modified
	directory_list_sorted = sorted(directory_list, key=operator.itemgetter(1), reverse=True)

	# find most recently modified directory
	dirstr = str(directory_list_sorted[0][0])
	
	# modify the string of the most recently modified directory to contain only the location
	last = dirstr.strip("'[]")
	
	# point towards the most recently edited players.dbf database
	location = (last + '\\' + 'players.dbf')

	# assign most recently modified players.dbf to the dbf module 
	ending_database = dbf.Table(location)
	
	ending_db = []
	
	# Convert ending_database to a list using dbf module
	with ending_database:
		
		index = ending_database.create_index (lambda rec: (rec.team))
		
		team = 0
		
		for x in range(50):
		
			matches = index.search (match= (team,), partial=True)
						
			for item in matches:
				
				ending_db.append([
										item[45],		# Team [0]
										item[2],		# First Name [1]
										item[1],		# Surname [2]
										item[46],		# Roster Position [3]
										
										item[122],		# Minutes [4]
										item[121],		# Turnovers [5]
										item[115],		# Blocks [6]
										item[119],		# Steals [7]
										format(item[116] + item[120]),		# Rebounds [8]
										item[117],		# Assists [9]
										format(((item[110]-item[112])*2) + (item[112]*3) + (item[114])),
														# Points [10]
										item[110],		# Field Goals [11]
										item[109],		# Field Goals Attempted [12]
										item[112],		# 3PT [13]
										item[111],		# 3PT Attempted [14]
										item[114],		# Free Throws [15]
										item[113],		# Free Throws Attempted [16]
										
										item[123],		# Games Played [17]
										item[4],		# Player ID [18]
										item[118],		# Personal Fouls [19]
										])
				
			team = team + 1

	# order the database of players by player_id
	ending_db_sorted = sorted(ending_db, key=operator.itemgetter(18))
	
	return ending_db_sorted
	
ending_db()
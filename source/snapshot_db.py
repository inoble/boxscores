import dbf, operator, os

def snapshot_db(db_id):
	""" Creates a snapshot of a database """

	# location of NBA Live 06 saved games
	target_dir = r'C:\Users\Ian\Documents\NBA Live 06\saves'
	
	directory_list = []

	# create a list of all directories available at location target_dir
	for d in os.listdir(target_dir):
		bd = os.path.join(target_dir, d)
		if os.path.isdir(bd): 
			directory_list.append([
								[bd],						# directory name
								[os.path.getmtime(bd)],		# time the directory was last modified
								])
	
	# sort in order of which directory was last modified
	directory_list_sorted = sorted(directory_list, key=operator.itemgetter(1), reverse=True)

	# find directory specified by db_id (0 = most recently modified, 1 = next most recent)
	dirstr = str(directory_list_sorted[db_id][0])
	
	# modify the string of the most recently modified directory to contain only the location
	last = dirstr.strip("'[]")
	
	# point towards the directory's players.dbf database
	location = (last + '\\' + 'players.dbf')

	# assign players.dbf to be processed by the dbf module 
	snapshot_database = dbf.Table(location)
	
	snapshot_db = []
	
	# Convert snapshot_database to a list of useful data using dbf module
	with snapshot_database:
		
		index = snapshot_database.create_index (lambda rec: (rec.team))
		
		team = 0
		
		for x in range(50):
		
			matches = index.search (match= (team,), partial=True)
						
			for item in matches:
				
				snapshot_db.append([
										item[45],							# Team [0]
										item[2],							# First Name [1]
										item[1],							# Surname [2]
										item[46],							# Roster Position [3]
										
										item[122],							# Minutes [4]
										item[121],							# Turnovers [5]
										item[115],							# Blocks [6]
										item[119],							# Steals [7]
										format(item[116] + item[120]),		# Rebounds [8]
										item[117],							# Assists [9]
										format(((item[110]-item[112])*2) + (item[112]*3) + (item[114])),
																			# Points [10]
										item[110],							# Field Goals [11]
										item[109],							# Field Goals Attempted [12]
										item[112],							# 3PT [13]
										item[111],							# 3PT Attempted [14]
										item[114],							# Free Throws [15]
										item[113],							# Free Throws Attempted [16]
										
										item[123],							# Games Played [17]
										item[4],							# Player ID [18]
										item[118],							# Personal Fouls [19]
										])
				
			team = team + 1

	# order the database of players by player_id
	snapshot_db_sorted = sorted(snapshot_db, key=operator.itemgetter(18))
	
	return snapshot_db_sorted


if __name__ == "__main__":

	snapshot_db(db_id)

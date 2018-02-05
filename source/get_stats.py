import operator
import snapshot_db

def get_stats():
	""" Creates every team's statistics for each game by subtracting an older from a newer database of stats """

	start_db = snapshot_db.snapshot_db(1)
	end_db = snapshot_db.snapshot_db(0)
	
	total_rows = len(start_db)
	
	subtracted = []
	
	team = 0
	
	for x in range(total_rows):
	
		subtracted.append([
						end_db[x][0],	# Team ID
						end_db[x][1],	# Player First Name
						end_db[x][2],	# Player Surname
						end_db[x][3],	# Player Roster Position
						format(int(end_db[x][4]) - int(start_db[x][4])),	# Minutes Played
						format(int(end_db[x][5]) - int(start_db[x][5])),	# Turnovers
						format(int(end_db[x][6]) - int(start_db[x][6])),	# Blocks
						format(int(end_db[x][7]) - int(start_db[x][7])),	# Steals
						format(int(end_db[x][8]) - int(start_db[x][8])),	# Rebounds
						format(int(end_db[x][9]) - int(start_db[x][9])),	# Assists
						format(int(end_db[x][10]) - int(start_db[x][10])),	# Points
						format(int(end_db[x][11]) - int(start_db[x][11])),	# Field Goals Made
						format(int(end_db[x][12]) - int(start_db[x][12])),	# Field Goals Attempted
						format(int(end_db[x][13]) - int(start_db[x][13])),	# Three-Pointers Made
						format(int(end_db[x][14]) - int(start_db[x][14])),	# Three-Pointers Attempted
						format(int(end_db[x][15]) - int(start_db[x][15])),	# Free Throws Made
						format(int(end_db[x][16]) - int(start_db[x][16])),	# Free Throws Attempted
						end_db[x][18],										# Player ID
						format(int(end_db[x][19]) - int(start_db[x][19])), 	# Personal Fouls
						])
	
	subtracted_sorted = sorted(subtracted, key=operator.itemgetter(0, 3))
	
	team = team + 1
	
	return subtracted_sorted


if __name__ == "__main__":

	get_stats()

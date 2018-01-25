import schedule_db, find_sims_date

def find_games():

	# list to contain all games on today's in-game date
	found_games = []

	# get list of league schedule
	schedule = schedule_db.schedule_db()
	
	# find today's in-game date
	game_date = find_sims_date.find_date()
	
	y = 0	
	
	# for every game on the schedule
	for x in schedule:
		
		schedule_date = schedule[y][0]
	
		# if game occurs on today's in-game date
		if schedule_date == game_date:
		
			found_games.append( [
								[schedule[y][0]],	# Date
								[schedule[y][1]],	# Time
								[schedule[y][2]],	# Home Team
								[schedule[y][3]],	# Away Team
								[schedule[y][4]],	# Home Score
								[schedule[y][5]],	# Away Score
								[schedule[y][7]],	# Overtime
								] )
								
		y = y + 1
	
	# return list of today's games information
	return found_games
		
find_games()
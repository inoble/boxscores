import schedule_db

def find_date():
	#import the league schedule as a list
	schedule = schedule_db.schedule_db()
	
	#find game date
	game_date = schedule[0][0]
	
	return game_date

find_date()
import schedule_db

def find_date():
	""" Finds the in-game date to be simulated """

	#import the league schedule as a list
	schedule = schedule_db.schedule_db()
	
	#find game date
	game_date = schedule[0][0]
	
	return game_date


if __name__ == "__main__":

	find_date()

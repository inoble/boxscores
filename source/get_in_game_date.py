import find_games

def get_in_game_date(game_number, irl_date):
	""" Finds the in-game date for which simulations are processed """

	games = find_games.find_games()
	
	in_game_day = int((str(games[game_number][0])[5:-1])[2:])

	in_game_month = int((str(games[game_number][0])[5:-1])[:-2])
	
	if in_game_month < 9:
	
		in_game_year = str(irl_date)[:-6]
		
	elif in_game_month > 9:
	
		in_game_year = int(str(irl_date)[:-6])-1
	
	game_date = str(str(in_game_year) + '-' + str(in_game_month) + '-' + str(in_game_day))
	
	return game_date

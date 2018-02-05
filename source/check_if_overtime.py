import find_games

def check_if_overtime(game_number):
	""" Checks whether a game went to "overtime" """
	
	games = find_games.find_games()

	is_overtime = str(games[game_number][6])

	if is_overtime == "[True]":
		overtime = 'OT'
	else:
		overtime = ''
		
	return overtime
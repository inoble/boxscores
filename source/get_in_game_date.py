import datetime
import find_games

def get_in_game_date(game_number):
	games = find_games.find_games()

	irl_date = datetime.date.today()
	in_game_month = int((str(games[game_number][0])[5:-1])[:-2])
	
	if in_game_month < 9:
		in_game_year = str(irl_date)[:-6]
	elif in_game_month > 9:
		in_game_year = int(str(irl_date)[:-6])-1
	
	in_game_date = str(in_game_year) + '-' + ((str(games[game_number][0])[5:-1])[:-2]) + '-' + ((str(games[game_number][0])[5:-1])[2:])
	
	print (in_game_date)
	
	return in_game_date

get_in_game_date()
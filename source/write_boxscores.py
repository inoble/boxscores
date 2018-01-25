import datetime
import get_stats, get_filename, find_games, teamdata

def write_boxscores():

	# import player statistics and today's games information
	stats = get_stats.get_stats()
	games = find_games.find_games()
	
	number_of_players = len(stats)
	number_of_games = len(games)
	
	# import teamdata for use in html presentation
	colours = teamdata.colours()
	jpgs = teamdata.jpgs()
	pngs = teamdata.pngs()
	teamnames = teamdata.teamnames()
	gm_names = teamdata.gm_names()
	gm_ids = teamdata.gm_ids()
	gm_awards = teamdata.gm_awards()
	
	# bbcode will be written to this file to be posted to the forum
	bbcode = open( r'C:\Users\Ian\Desktop\boxscores.txt', 'w' )
	
	for x in range(number_of_games):
	
		# each game is assigned a separate filename for upload to webserver
		filename = get_filename.get_filename()
		
		# configure dates for presentation
		# real life date on which the games are simulated
		irl_date = str(datetime.date.today())
		
		def generate_in_game_date():
		
			in_game_month = int((str(games[x][0])[5:-1])[:-2])
			
			if in_game_month < 9:
				in_game_year = str(irl_date)[:-6]
			elif in_game_month > 9:
				in_game_year = int(str(irl_date)[:-6])-1
			
			game_date = str(str(in_game_year) + '-' + ((str(games[x][0])[5:-1])[:-2]) + '-' + ((str(games[x][0])[5:-1])[2:]))
			
			return game_date

		# in-game date on which the games are simulated
		in_game_date = generate_in_game_date()			
			
		# check if game went to overtime
		def check_if_overtime():
		
			is_overtime = str(games[x][6])
		
			if is_overtime == "[True]":
				overtime = 'OT'
			else:
				overtime = ''
				
			return overtime
		
		overtime = check_if_overtime()
		
		# assign home and away team variables
		game_time = str(games[x][1])[1:-1]
		home_team = int(str(games[x][2])[1:-1])
		away_team = int(str(games[x][3])[1:-1])
		home_score = str(games[x][4])[1:-1]
		away_score = str(games[x][5])[1:-1]
		
		home_team_string = teamnames[home_team]
		away_team_string = teamnames[away_team]
		home_gm_name = str(gm_names[home_team])
		away_gm_name = str(gm_names[away_team])
		home_gm_id = str(gm_ids[home_team])
		away_gm_id = str(gm_ids[away_team])
		home_gm_awards = str(gm_awards[home_team])
		away_gm_awards = str(gm_awards[away_team])

		# write bbcode to be posted on the forum
		bbcode.write (
			'[a href="http://www.iannoble.org.uk/d5/scores/1718/bx' + filename + '"]' + '[img]http://iannoble.org.uk/d5/box.gif[/img][/a] ' + teamnames[away_team] + ' @ ' + teamnames[home_team] + '\n'
					)			
		
		# html code will be written to this file and uploaded to the webserver
		boxscore = open( r'C:\Users\Ian\OneDrive\Ian\Documents\Dynasty Five\Results\1718\bx' + filename, 'w' )
		
		# write html file
		boxscore.write (
		
			# write html title, assign favicon and css
			'<html><head><title>' + teamnames[away_team] + ' @ ' + teamnames[home_team] + '</title>'
			'<link rel="shortcut icon" href="http://www.iannoble.org.uk/d5/images/favicon.ico">'
			'<link rel=stylesheet type=text/css href=website/style.css />'
			'</head>'
			
			# write navigation links back to homepage and previous page
			'<body><center><box>'
			'<nav_bar_img><a href=http://www.dynastyfive.com><img src="http://www.iannoble.org.uk/d5/images/54x31%20nav%20bar%20img.png"></a></nav_bar_img>'
			'<header_text><a href=javascript:history.back()><font color=0077cb>< back</font></a></header_text>'
			
			# write team and score @ score and team
			'<boxscore><table width="800px"><tr>'
			'<td width=275></td>'
			'<td width=50><center><img src=http://iannoble.org.uk/d5star/logos/' + pngs[away_team] + '></center></td>'
			'<td width=50><center><font color=ffffff>' + overtime + '</font></center></td>'
			'<td width=50><center><img src=http://iannoble.org.uk/d5star/logos/' + pngs[home_team] + '></center></td>'
			'<td width=275></td>'
			'</tr></table>'
			'<table width=800px><tr>'
			'<td width=275><div align="right"><b><font size="4" color=' + colours[away_team] + '>' + away_team_string + '</font></b></div></td>'
			'<td width=50><center><font size="6" color=' + colours[away_team] + '>' + away_score + '</font></center></td>'
			'<td width=50><center><font color=ffffff>@</font></center></td>'
			'<td width=50><center><font size="6" color=' + colours[home_team] + '>' + home_score + '</font></center></td>'
			'<td width=275><b><font size="4" color=' + colours[home_team] + '>' + home_team_string + '</font></b></td>'
			'</tr>'
			
			# write general manager and team record information
			'<tr><td width=275><div align="right">' + away_gm_awards + ' <a href="http://dynasty5ive.proboards.com/user/' + away_gm_id + '"><font size=3 color=0077cb>' + away_gm_name + '</font></a></div></td>'
			'<td colspan=3 width=150></td>'
			'<td width=275><a href="http://dynasty5ive.proboards.com/user/' + home_gm_id + '"><font size=3 color=0077cb>' + home_gm_name + '</font></a> ' + home_gm_awards + '</td>'
			'</tr></table>'

			# write dates and time
			'<table width=800px><tr><td colspan=13></td></tr>'
			'<tr>'
			'<td width=350><font size=1 color=ffffff>SIM DATE: ' + irl_date + '</font></td>'
			'<td width=100><font size=1 color=ffffff><center>TIP-OFF: ' + game_time + '</center></font></td>'
			'<td width=350><div align=right><font size=1 color=ffffff>D5 DATE: ' + in_game_date + '</font></div></td>'
			'</tr></table>'
		
						)
		
		# statistics totals
		fgat, fgmt, tpat, tpmt, ftat, ftmt, tovt, blkt, stlt, rebt, astt, ptst, fgata, fgmta, tpata, tpmta, ftata, ftmta, tovta, blkta, stlta, rebta, astta, ptsta = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

		teams_playing = [ away_team, home_team ]
		
		# for loop for each team playing
		for z in range(2):
		
			team_to_write = teams_playing[z]
			
			# declare list of statistics column headers in preparation for writing as a for loop
			boxscore_header_cells = [ 'Min', 'FG', '3PT', 'FT', 'PF', 'TO', 'Blk', 'Stl', 'Reb', 'Ast', 'Pts' ]
			
			boxscore.write ('<table width="800px"><tr><td></td><td></td>')
			
			# write each statistics column header
			for item in range(len(boxscore_header_cells)):
				
				boxscore.write ( '<td><b><font size=2 color="' + str(colours[team_to_write]) + '"><center>' + boxscore_header_cells[item] + '</center></font></b></td>' )
								
			boxscore.write ('</tr>')
			
			# check through each player in the database
			for y in range(number_of_players):

				# assign player statistics variables
				first_name = str(stats[y][1])
				surname = str(stats[y][2])
				full_name = (first_name + ' ' + surname)
				
				mins = str(stats[y][4])
				tov = str(stats[y][5])
				blk = str(stats[y][6])
				stl = str(stats[y][7])
				reb = str(stats[y][8])
				ast = str(stats[y][9])
				pts = str(stats[y][10])
				fouls = str(stats[y][18])
				
				fgm = str(stats[y][11])
				tpm = str(stats[y][13])
				ftm = str(stats[y][15])
				fga = str(stats[y][12])
				tpa = str(stats[y][14])
				fta = str(stats[y][16])
				fg = (fgm + '/' + fga)
				tp = (tpm + '/' + tpa)
				ft = (ftm + '/' + fta)
				
				# write player statistics if team is found
				if team_to_write == stats[y][0]:
					
					# write each player's name in first column
					boxscore.write ( '<tr>'
							'<td width=150><font size=2 color=' + str(colours[team_to_write]) + '>' + full_name + '</font></td>'
							'<td></td>' )
					
					# declare list of statistics in preparation for writing as a for loop
					player_stats_cells = [ mins, fg, tp, ft, fouls, tov, blk, stl, reb, ast, pts ]
					
					# write each player's statistics for each player found
					for item in range(len(player_stats_cells)):
						
						boxscore.write ( '<td width=50><center><font size=2 color=ffffff>' + player_stats_cells[item] + '</font></center></td>' )
					
					# close row
					boxscore.write ( '</tr>' )
					
					# calculate team totals whilst writing each player's statistics
					fgata = fgata + int(fga)
					fgmta = fgmta + int(fgm)
					tpata = tpata + int(tpa)
					tpmta = tpmta + int(tpm)
					ftata = ftata + int(fta)
					ftmta = ftmta + int(ftm)
					tovta = tovta + int(tov)
					blkta = blkta + int(blk)
					stlta = stlta + int(stl)
					rebta = rebta + int(reb)
					astta = astta + int(ast)
					ptsta = ptsta + int(pts)
					
					fgata_str = (str(fgmta) + '/' + str(fgata))
					tpata_str = (str(tpmta) + '/' + str(tpata))
					ftata_str = (str(ftmta) + '/' + str(ftata))					
					tovtsa = str(tovta)
					blktsa = str(blkta)
					stltsa = str(stlta)
					rebtsa = str(rebta)
					asttsa = str(astta)
					ptstsa = str(ptsta)
					
			# write team statistical totals as a for loop
			boxscore.write ( '<tr><td width=150><font size=2 color="' + str(colours[team_to_write]) + '"><b>Totals</b></font></td></td>' )
			
			# declare list of statistics totals in preparation for writing as a for loop
			team_total_strings = [ '', '', fgata_str, tpata_str, ftata_str, '', tovtsa, blktsa, stltsa, rebtsa, asttsa, ptstsa  ]
			
			# write team's statistics totals
			for item in range(len(team_total_strings)):
			
				boxscore.write ( '<td width=50><font size=2 color="' + str(colours[team_to_write]) + '"><b><center>' + team_total_strings[item] + '</center></b></font></td>' )
				
			# spacing between away and home team boxscores
			boxscore.write ( '</tr><tr><td colspan=13><font color=00091f>|</font></td></tr>' )
			
			# reset statistics totals back to zero before next team is posted
			tovta, blkta, stlta, rebta, astta, ptsta, fgata, fgmta, tpata, tpmta, ftata, ftmta = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
			
		# end of boxscore
		boxscore.write ( '</table></boxscore></box></center></body></html>' )
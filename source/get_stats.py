import operator
import starting_db, ending_db

def get_stats():	
	start_db = starting_db.starting_db()
	end_db = ending_db.ending_db()
	
	total_rows = len(start_db)
	
	subtracted = []
	
	team = 0
	
	for x in range(total_rows):
	
		subtracted.append([
						end_db[x][0],
						end_db[x][1],
						end_db[x][2],
						end_db[x][3],
						format(int(end_db[x][4]) - int(start_db[x][4])),
						format(int(end_db[x][5]) - int(start_db[x][5])),
						format(int(end_db[x][6]) - int(start_db[x][6])),
						format(int(end_db[x][7]) - int(start_db[x][7])),
						format(int(end_db[x][8]) - int(start_db[x][8])),
						format(int(end_db[x][9]) - int(start_db[x][9])),
						format(int(end_db[x][10]) - int(start_db[x][10])),
						format(int(end_db[x][11]) - int(start_db[x][11])),
						format(int(end_db[x][12]) - int(start_db[x][12])),
						format(int(end_db[x][13]) - int(start_db[x][13])),
						format(int(end_db[x][14]) - int(start_db[x][14])),
						format(int(end_db[x][15]) - int(start_db[x][15])),
						format(int(end_db[x][16]) - int(start_db[x][16])),
						end_db[x][18],
						format(int(end_db[x][19]) - int(start_db[x][19])), # Personal Fouls [18]
						])
	
	#test_subtracted_db = open(r'C:\Users\Ian\Desktop\Py\WIP\boxscores\subtracted.txt', 'w')
	#test_subtracted_db.write ( str(subtracted) )
	
	subtracted_sorted = sorted(subtracted, key=operator.itemgetter(0, 3))
	
	team = team + 1
	
	return subtracted_sorted

get_stats()
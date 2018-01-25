import os, operator

def find_files():

	# location of all previously created html files
	target_dir = r'C:\Users\Ian\OneDrive\Ian\Documents\Dynasty Five\Results\1718'

	files = []

	# create list of all files in the directory
	for d in os.listdir(target_dir):
		bd = os.path.join(target_dir, d)
		if os.path.isfile(bd): 
			files.append([
								[bd],
								])
	
	# sort files by filename to find most recently edited	
	starting_files = sorted(files, key=operator.itemgetter(0), reverse=True)
	
	return starting_files
	
find_files()
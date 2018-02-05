import os, operator

def get_filename():
	""" Generates the next html filename to be created """

	target_dir = r'C:\Users\Ian\OneDrive\Ian\Documents\Dynasty Five\Results\1718'

	files = []

	# Find most recently edited directory.
	for d in os.listdir(target_dir):
		bd = os.path.join(target_dir, d)
		if os.path.isfile(bd): 
			files.append([
								[bd],
								[os.path.getmtime(bd)],
								])
	
	files_sorted = sorted(files, key=operator.itemgetter(0), reverse=True)
	
	last_file_name = 0
	
	# if no files, create original file
	if not files_sorted:
	
		next_file_name = '0000.html'
	
	else:
		# the following line of code:
		# 1) selects the newest file in the directory (files_sorted[0][0])
		# 2) returns the filename of the file as a string and strips all but the last 11th to 7th characters
		# 3) turns the characters into an integer
		# 4) adds 1 to the integer
		last_file_name = int((str(files_sorted[0][0]))[-11:-7]) + 1
	
		if len(str(last_file_name)) == 1:
			
			next_file_name = '000' + str(last_file_name) + '.html'
		
		elif len(str(last_file_name)) == 2:

			next_file_name = '00' + str(last_file_name) + '.html'

		elif len(str(last_file_name)) == 3:

			next_file_name = '0' + str(last_file_name) + '.html'

		elif len(str(last_file_name)) == 4:

			next_file_name = str(last_file_name) + '.html'
		
	return next_file_name
	

if __name__ == "__main__":

	get_filename()

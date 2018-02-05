import os, pyperclip, time
import find_files, write_boxscores
from ftplib import FTP

# snapshot of the directory before files are created
start = find_files.find_files()

# file and bbcode creation
write_boxscores.write_boxscores()

# snapshot of the directory after files are created
end = find_files.find_files()

# create a list containing only the files just created
created_boxscores = [x for x in end if x not in start]

def upload_boxscores(ftp = FTP('server.name'), ftp_user='username', ftp_passwd='password', upload_directory = 'server\\directory\\location'):
	""" Uploads every newly created html file """

	# declare ftp settings
	ftp.login(user=ftp_user, passwd=ftp_passwd)
	ftp.cwd(upload_directory)
	
	# upload each newly created file
	for x in created_boxscores:
	
		# strip excess file location string before upload
		file_to_upload = str(x)[74:-3]
	
		print ('uploading: ' + file_to_upload)
		
		# set default directory containing created files
		os.chdir(r'C:\Users\Ian\OneDrive\Ian\Documents\Dynasty Five\Results\1718')
		
		# upload files
		ftp.storbinary('STOR ' + file_to_upload, open(file_to_upload, 'rb'))


def copy_bbcode_to_clipboard():		
	""" Copies presentable bbcode game-links to the clipboard for pasting into online forum """
	
	# file to copy
	bbcode = open(r'C:\Users\Ian\Desktop\boxscores.txt', 'r').read()
	
	# copy command
	pyperclip.copy(bbcode)
	
	print ('bbcode copied and ready to paste')
	
	time.sleep(2)


if __name__ == "__main__":

	upload_boxscores()
	
	copy_bbcode_to_clipboard()

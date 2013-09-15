import sys
import os
import glob
import datetime
import shutil


#count args
if len(sys.argv) != 3:
	print("ERROR: Organizer requires two arguments: A path and a file type.")
	exit(1)

#verify folder exists
path = sys.argv[1]
filetype = sys.argv[2]

if not os.path.exists(path):
	print("Path", path, "does not exist.")
	exit(1)

#read all jpg files in the directory
os.chdir(path)
files = glob.glob("*." + filetype)

for f in files:
	time = os.path.getmtime(f) 
	date = str(datetime.date.fromtimestamp(time))
	
	#create new folder if it does not already exist
	if not os.path.exists(date):
		os.makedirs(date)

	#move file to new folder
	dst = date + "\\" + f
	shutil.move(f, dst)	
import sys
import os
import glob


#count args
if len(sys.argv) != 2:
	print("ERROR: Organizer requires one path as an argument.")
	exit(1)

#verify folder exists
path = sys.argv[1]

if not os.path.exists(path):
	print("Path", path, "does not exist.")
	exit(1)

#read all jpg files in the directory
os.chdir(path)
files = glob.glob("*.jpg")

for f in files: 
	print(f)
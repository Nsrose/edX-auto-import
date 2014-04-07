### Comprehensive lab parser ### 
from new_lab_parser import * 
from tar_file import *
import shutil, os

### helper functions ###

def move_files(filename, src_folder):
	shutil.copy(filename[:-6] + ".xml", src_folder + "/sequential")
	for f in os.listdir("html"):
		shutil.copy("html/" + f, src_folder + "/html")
	for f in os.listdir("vertical"):
		shutil.copy("vertical/" + f, src_folder + "/vertical")

### staging ###

os.system("clear")
print("#############################")
print("Lab Parser")
print("Version 1.0")
print("#############################")
print("\n")
print("Instructions:")
print("1) Make sure current directory contains bjc-r, edX course folder, and .topic lab to parse.")
print("2) Add the sequential filename to the appropriate place in course/chapter folder BEFORE parsing.")
print("\n")
print("Current directory contains:")
print("\n")

files = [f for f in os.listdir('.')]
if "bjc-r" not in files:
	print("---bjc-r folder not found in current directory. Parsing cancelled.")
	sys.exit()
for f in files:
	print(f)
print("\n")
print("Enter each lab you want to parse.")
print("'q' ---finish")
print("'.' ---add all labs in current folder")
print("\n")

labs = []
done = False
while not done:
	lab_source = input("Lab file name, including .topic: ")
	if lab_source.lower() == 'q':
		print("---All labs ready for parsing: " + str(labs))
		done = True
	elif lab_source == '.':
		for f in files:
			if ".topic" in f:
				labs.append(f)
		print("---Staged all labs in current directory: " + str(labs))
		done = True
	elif ".topic" not in lab_source:
		print("---Must parse .topic file only.")
	else:
		try:
			dummy = open(lab_source, 'r').read()
			labs.append(lab_source)
			print("---Added.")
		except:
			print("---Invalid input.")

print("\n")
done1 = False
while not done1:
	course_folder = input("Course folder name: ")
	try:
		dummy = os.listdir(course_folder)
		done1 = True
	except:
		print("---Invalid folder selection.")
print("\n")

### execution ###

for lab in labs:
	print("Adding lab " + lab[:-6] + "...")
	parse(lab)
	move_files(lab, course_folder)
	shutil.rmtree('vertical')
	shutil.rmtree('html')
	os.remove(lab[:-6] + ".xml")
	print("Parsed lab " + lab[:-6] + '.')
	print("\n")

print("Creating new .tar.gz file for import...")
tarred_file = course_folder + ".tar.gz"
if os.path.exists(tarred_file):
	os.remove(tarred_file)

make_tarfile(tarred_file, course_folder)
print("Course file ready for import.")
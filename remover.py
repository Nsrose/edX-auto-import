### Comprehensive lab remover ### 
import shutil, os
from new_lab_parser import * 
from tar_file import *

### helper functions ###

def remove_file(folder, filename):
	"""Removes file filename from folder, if it exists"""
	if os.path.exists(folder + "/" + filename):
		os.remove(folder + "/" + filename)

def remove_lab(lab_name, course_folder):
	"""Psuedo creates a new lab, in order to remove it from the course folder"""
	folders()
	make_sequential(lab_name)
	pure_name = lab_name[:-6]
	remove_file(course_folder + "/sequential", pure_name + ".xml")
	for f in os.listdir("html"):
		remove_file(course_folder + "/html", f)
	for f in os.listdir("vertical"):
		remove_file(course_folder + "/vertical", f)
	shutil.rmtree('vertical')
	shutil.rmtree('html')
	os.remove(pure_name + ".xml")

### staging ###

os.system("clear")
print("#############################")
print("Lab Remover")
print("Version 1.0")
print("#############################")
print("\n")
print("Instructions:")
print("1) Make sure current directory contains bjc-r, edX course folder, and .topic lab to remove.")
print("2) Remove the sequential filename from the appropriate place in course/chapter folder BEFORE parsing.")
print("\n")
print("Current directory contains:")
print("\n")

files = [f for f in os.listdir('.')]
if "bjc-r" not in files:
	print("---bjc-r folder not found in current directory. Removing cancelled.")
	sys.exit()
for f in files:
	print(f)
print("\n")
print("Enter each lab you want to remove.")
print("'q' ---finish")
print("'.' ---remove all labs in current folder")
print("\n")

labs = []
done = False
while not done:
	lab_source = input("Lab file name, including .topic: ")
	if lab_source.lower() == 'q':
		print("---All labs ready for removal: " + str(labs))
		done = True
	elif lab_source == '.':
		for f in files:
			if ".topic" in f:
				labs.append(f)
		print("---Staged all labs in current directory: " + str(labs))
		done = True
	elif ".topic" not in lab_source:
		print("---Must remove .topic file only.")
	else:
		try:
			dummy = open(lab_source, 'r').read()
			labs.append(lab_source)
			print("---Staged.")
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
	print("Removing lab " + lab[:-6] + "...")
	remove_lab(lab, course_folder)
	print("Removed lab " + lab[:-6] + '.')
	print("\n")

print("Creating new .tar.gz file for import...")
tarred_file = course_folder + ".tar.gz"
if os.path.exists(tarred_file):
	os.remove(tarred_file)

make_tarfile(tarred_file, course_folder)
print("Course file ready for import.")

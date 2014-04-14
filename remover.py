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
print("Version 1.5")
print("#############################")
print("\n")
print("Instructions:")
print("1) Make sure current directory contains bjc-r and edX course folder from export.")
print("2) Remove the sequential filename from the appropriate place in course/chapter folder BEFORE parsing.")
print("\n")

### navigation to folder ###
done0 = False
labs = []
while not done0:
	print("\n")
	print("Type a folder to browse topic files to remove.")
	print("'w' ---finish staging labs")
	print("'s' ---show currently staged labs")
	print("\n")
	files = [f for f in os.listdir('.')]
	if "bjc-r" not in files:
		print("---bjc-r folder not found in current directory. Parsing cancelled.")
		sys.exit()
	for folder in os.listdir('bjc-r/topic/berkeley_bjc'):
		print(folder)
	print("\n")
	folder = input("Enter folder name to navigate: ")
	if folder.lower() == 'w':
		done0 = True 
		print("---All labs ready for removal: " + str(labs))
	elif folder.lower() == 's':
		print("Currently staged labs: " + str(labs))
	else:
		try:
			folder = 'bjc-r/topic/berkeley_bjc/' + folder 
			files = [f for f in os.listdir(folder)]
			
			### choosing labs to parse ###
			print("\n")
			print("Enter each lab you want to remove.")
			print("'q' ---finish")
			print("'.' ---stage all labs in current folder")
			print("'b' ---go back")
			print("\n")
			for f in files:
				print(f)
			print("\n")
			done = False
			while not done:
				lab_source = input("Lab file name, including .topic: ")
				if lab_source.lower() == 'q':
					print("---All labs ready for removal: " + str(labs))
					done = True
				elif lab_source == '.':
					for f in files:
						if ".topic" in f:
							labs.append(folder + "/" + f)
					print("---Staged all labs in current directory: " + str(labs))
					done = True
				elif lab_source.lower() == 'b':
					done = True 
				elif lab_source.lower() == 's':
					print("Currently staged labs: " + str(labs))
				elif ".topic" not in lab_source:
					print("---Must remove .topic file only.")
				else:
					try:
						dummy = open(folder + "/" + lab_source, 'r').read()
						labs.append(folder + "/" + lab_source)
						print("---Staged.")
					except:
						print("---Invalid input.")
		except:
			print("No such folder exists.")


### Course folder selection ###
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
	psuedo_topic = lab.rsplit('/', 1)[1]
	print("Removing lab " + psuedo_topic + "...")
	touch(psuedo_topic)
	shutil.copy(lab, psuedo_topic)
	remove_lab(psuedo_topic, course_folder)
	os.remove(psuedo_topic)
	print("Removed lab " + psuedo_topic + '.')
	print("\n")


print("Creating new .tar.gz file for import...")
tarred_file = course_folder + ".tar.gz"
if os.path.exists(tarred_file):
	os.remove(tarred_file)

make_tarfile(tarred_file, course_folder)
print("Course file ready for import.")
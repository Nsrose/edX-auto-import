edX-auto-import
===============

Import Testing for BJC edX Course dev

Lab Parser v 1.0

Parses labs from bjc-r into an entirely new course file ready for edX import 

Instructions:

===============

Parsing:

---------------

1) Make sure parser.py, tar_file.py, new_lab_parser.py, the course folder, bjc-r, and the .topic lab(s) you want to parse all are in your current directory.

---If lab doesn't already exist in course:
2) Add the name of the lab (without the .topic) as a sequential filename to the correct chapter in the course folder. 

---If lab does exist, and you are modifying an existing lab:
2) Don't need to add the name of the lab to the correct chapter in the course folder.


3) Run parser.py and follow onscreen instructions.

4) Go to studio.edge.edx.org and import the newly created {{Course Folder}}.tar.gz file.

Removing:

---------------

1) Make sure current directory contains parser.py, tar_file.py, new_lab_parser.py, course folder, bjc-r, the .topic labs to remove, and remover.py.

2) You can remove the name of the lab from the correct chapter in the course folder if you want to for ease of reading, but this isn't a necessary step. 

3) Run remover.py and follow onsceen instructions.

4) Go to studio.edge.edx.org and import the newly created {{Course Folder}}.tar.gz file.



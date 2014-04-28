import os, sys
from os import listdir
from os.path import isfile, join
from shutil import copyfile, move 
from functools import reduce


#########################################
## Backend Lab Parser for Berkeley BJC ##
#########################################


### Creates folders containing the necessary items to import into an edX course ###
### Should make a sequential file, a folder of vertical files, and a folder of html files ###



### trigger tags ###
	### set of tags that should note where a certain piece of info lies ###
	### please add to this set ### 
tags = {"title:", "resource:", "quiz:", "assignment:", "group:", "forum:", "video:", "reading:", "big-idea:", "learning-goal:"}
vertical_tags = {"resource:", "assignment:", "group:", "forum:"}
#NOTE: vertical_tag "quiz" is removed for now because quiz parser isn't working yet #

### helper functions ###

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def folders():
	new_paths = [r'vertical', r'html']
	for path in new_paths:
		if not os.path.exists(path):
			os.makedirs(path)

def get_inner_content(line, start_char=None, end_char=None):
	"""Returns an additive string between two tags"""
	result = ''
	words = line.split()
	for word in words:
		if word not in tags and word!=start_char and word!=end_char:
			result += word + ' '
	return result[:-1]  

def get_title(filename):
	"""Grabs the title of the whole lab"""
	content = open(filename, 'r')
	title_line = content.readline()
	return get_inner_content(title_line)

def insert_title(title, lines):
	"""Returns a title-inserted version of the html input"""
	for i in range(len(lines)):
		if "<body>" in lines[i]:
			lines.insert(i+1, '<h1>' + title + '</h1>')
			return lines 
	return "<body> Not Found"

def make_companion_xml(name, title):
	"""Makes the corresponding xml file for an html file"""
	touch('html/' + name + ".xml")
	target = open('html/' + name + ".xml", 'a')
	line0 = '<html filename="' + name + '" display_name="' + title.replace('"', '') + '"/>'
	target.write(line0)
	target.close	

def count_special(el_inline):
	"""Counts src and hrefs in a list line"""
	return len(list(filter(lambda x: "src" in x or "href" in x, el_inline)))

def separate_elements(el_inline):
	"""Separates list element of multiple links to several lists of one link"""
	if count_special(el_inline) < 2:
		return [el_inline] 
	else:
		end = [] 
		while count_special(el_inline)>1:	
			index = 0
			result = []
			while "src" not in el_inline[index] and "href" not in el_inline[index]:
				result += [el_inline[index]]
				index += 1 
			result += [el_inline[index]]
			end.append(result)
			el_inline = el_inline[index+1:]
		end.append(el_inline)
		return end 


def remove_whitespace(el_inline):
	"""Changes src = to src= in a split line"""
	result = []
	i = 0
	while i<len(el_inline):
		if el_inline[i] == "href" or el_inline[i] == "src":
			if el_inline[i+1] == "=":
				modded = el_inline[i] + el_inline[i+1] + el_inline[i+2]
				result.append(modded)
				i += 3
			else:
				modded = el_inline[i] + el_inline[i+1]
				result.append(modded)
				i += 2 
		elif el_inline[i] == "href=" or el_inline[i] == "src=":
			modded = el_inline[i] + el_inline[i+1]
			result.append(modded)
			i += 2
		else:
			result.append(el_inline[i])
			i += 1 
	return result 

def fix_links(lines):
	"""Changes relative to absolute links within html page"""
	result = []
	for line in lines:
		if "href" in line:
			el_inline = line.split() 
			el_inline = remove_whitespace(el_inline)
			el_inline = separate_elements(el_inline)
			for el in el_inline:	
				index = 0
				while "href" not in el[index]:
					index += 1
				relevant = el[index]
				if "http" in relevant:
					new_line = ' '.join(el)
					result.append(new_line)
				else:
					relevant = relevant.replace('href="', '')
					if "../" in relevant:
						modded_element = 'href=' + '"http://inst.eecs.berkeley.edu/~cs10/labs/' + relevant.replace("../", "")
					elif '/bjc-r' in relevant:
						modded_element = 'href=' + '"http://bjc.berkeley.edu' + relevant
					elif '#' in relevant:
						modded_element = 'href=' + relevant
					else:
						modded_element = 'href=' + '"http://bjc.berkeley.edu/' + relevant
					el[index] = modded_element
					new_line = ' '.join(el)
					result.append(new_line)
		
		elif "src" in line:
			el_inline = line.split() 
			el_inline = remove_whitespace(el_inline)
			el_inline = separate_elements(el_inline)
			for el in el_inline:			
				index = 0
				while "src" not in el[index]:
					index += 1
				relevant = el[index]
				if "http" in relevant:
					new_line = ' '.join(el)
					result.append(new_line)
				else:
					relevant = relevant.replace('src="', '')
					if "../" in relevant:
						modded_element = 'src=' + '"http://inst.eecs.berkeley.edu/~cs10/labs/' + relevant.replace("../", "")
					elif '/bjc-r' in relevant:
						modded_element = 'src=' + '"http://bjc.berkeley.edu' + relevant
					elif '#' in relevant:
						modded_element = 'src=' + relevant
					else:
						modded_element = 'src=' + '"http://bjc.berkeley.edu/' + relevant
					el[index] = modded_element
					new_line = ' '.join(el)
					result.append(new_line)
		else:
			result.append(line)
	return result 


def process_quiz(lines):
	"""Converts html into proper edX format for quiz"""
	new_lines = []
	start = lines.index("<html>")
	end = lines.index("<body>") + 1
	new_lines += lines[start:end]
	
	new_lines += ["<problem>"]
	start_index = lines.index('<div class="prompt">')
	for i in range(start_index, len(lines)):
		if lines[i] == '</div>':
			endx = i 
			break
	for line in lines[start_index:endx+1]:
		new_lines += [line]
	new_lines += ['<multiplechoiceresponse>', '<choicegroup type="MultipleChoice">']
	
	## finding correct choice ##
	for i in range(len(lines)):
		if 'class="correctResponse"' in lines[i]:
			c_index = i
			break
	correct_line = lines[c_index]
	f = lambda x: 'identifier' in x
	l = list(filter(f, correct_line.split()))[0]
	l = l.rsplit('=', 1)[1]
	correct_choice = l.rstrip('></div>')
	############################

	for i in range(len(lines)):
		line = lines[i]
		if '<div class="choice"' in line:
			choice = line.split()[2].rsplit('=', 1)[1].rstrip('>')
			inner_content = lines[i+2:i+3].pop()	
			if choice == correct_choice:
				new_lines += ['<choice correct="true">' + inner_content + "</choice>"]
			else:
				new_lines += ['<choice correct="false">' + inner_content + "</choice>"]
	new_lines += ['</choicegroup>', '</multiplechoiceresponse>', '<solution>']
	new_lines += ['<div class="detailed_solution">', '<p>Explanation</p>']

	### feedback ###
	for i in range(len(lines)):
		if 'identifier=' + correct_choice + '>' in lines[i]:
			start_index = i
			break
	k = start_index
	while k < len(lines):
		k += 1
		if "</div>" in lines[k]:
			endx = k
			break
	start_index = endx + 2
	k = start_index
	while k < len(lines):
		k += 1
		if "</div>" in lines[k]:
			endx = k
			break
	feedback = lines[start_index:endx]
	new_lines += feedback
	new_lines += ['</div>', '</solution>', '</problem>', '</body>', '</html>']
	return new_lines 




def insert_snap(lines):
	"""Inserts snap iframe to top of html page"""
	for i in range(len(lines)):
		if '<head>' in lines[i]:
			index = i 
			break
	iframe = open("snap-frame.html", 'r')
	ilines = iframe.read()
	lines.insert(index, ilines)
	return lines 



def make_html(line):
	"""Makes an html and corresponding xml file from a line--
	must already have created html folder"""
	path_content = line.split()[-1]
	absolute_path = path_content[2:-1]
	name = absolute_path.rsplit('/', 1)[1][:-5]
	title = get_inner_content(line, None, path_content)

	make_companion_xml(name, title)
	destination = 'html/' + name + ".html"
	touch(destination)
	copyfile(absolute_path, destination) 

	## adding in a title for the lab ##
	try:
		content = open(destination, 'r')
		lines = content.readlines() 
		lines = [x for x in [s.strip() for s in lines] if not x == '']
		lines = insert_title(title, lines)
		### check for quiz ###
		for line in lines:
			if "assessment-data" in line:
				# lines = process_quiz(lines)

				break
		
		lines = fix_links(lines)
		lines = insert_snap(lines)
		new_file = open(destination, 'w') 
		new_content = (' ').join(lines)
		new_file.write(new_content)
	except:
		pass 


def make_overview(filename):
	"""Makes an overview html and xml file, as well as vertical file. 
	Must already have html folder"""

	content = open(filename, 'r')
	lines = content.readlines()
	lines = [x for x in [s.strip() for s in lines] if not x == '']


	name = filename[:-6]
	make_companion_xml("overview" + name, "Overview")
	destination = 'html/' + "overview" + name + ".html"
	touch(destination)
	target = open(destination, 'a')
	target.write("<html>")
	target.write("\n")
	target.write("<h1>Overview</h1>")
	target.write("\n")
	target.write("<h2>Big Ideas</h2>")
	target.write("\n")
	target.write("<ul>")
	target.write("\n")

	def make_li(line):
		result = "<li>"
		result += get_inner_content(line)
		return result + "</li>"

	for line in lines:
		if line.split()[0] == "big-idea:":
			target.write(make_li(line))
			target.write("\n")
	target.write("</ul>")
	target.write("\n")

	target.write("<h2>Activites</h2>")
	target.write("\n")
	target.write("<ul>")
	target.write("\n")
	for line in lines:
		if line.split()[0] == "learning-goal:":
			target.write(make_li(line))
			target.write("\n")
	target.write("</ul>")
	target.write("\n")
	target.write("</html>")

	## add vertical companion ##
	touch("vertical/overview" + name + ".xml")
	target_new = open("vertical/overview" + name + ".xml", 'a')
	target_new.write('<vertical display_name="Overview">')
	target_new.write("\n")
	target_new.write('	<html url_name="overview' + name + '"/>')
	target_new.write("\n")
	target_new.write("</vertical>")

def get_quote(name):
	"""Takes in a name with/without quotes, and returns either ' or ", depending."""
	if '"' in name:
		return "'"
	return '"'

def make_vertical(name, line):
	"""makes a vertical file in the vertical folder"""
	touch("vertical/" + name + ".xml")
	target = open("vertical/" + name + ".xml", 'a')
	path_content = line.split()[-1]	
	title = get_inner_content(line, None, path_content)
	absolute_path = path_content[2:-1]
	html_name = absolute_path.rsplit('/', 1)[1][:-5]

	quote = get_quote(title)
	target.write("<vertical display_name=" + quote + title + quote + ">")
	target.write("\n")
	target.write('	<html url_name="' + html_name + '"/>')
	target.write("\n")
	target.write("</vertical>")

def make_sequential(filename):
	"""Makes the sequential file. Must add to correct chapter manually."""
	content = open(filename, 'r')
	lines = content.readlines()
	lines = [x for x in [s.strip() for s in lines] if not x == '']

	seq_name = filename[:-6] + ".xml"
	display_name = get_title(filename)
	touch(seq_name)
	target = open(seq_name, 'a')
	target.write('<sequential display_name="' + display_name + '">')
	target.write("\n")
	target.write('<vertical url_name="overview' + filename[:-6] + '"/>')
	target.write("\n")
	last_line = "</sequential>"
	
	make_overview(filename)

	for index in range(len(lines)):
		if lines[index].split()[0] in vertical_tags:
			current_name = filename[:-6] + str(index)
			target.write('<vertical url_name="' + current_name + '"/>')
			target.write("\n")
			make_vertical(current_name, lines[index])
			make_html(lines[index])
	target.write(last_line)

### Execution ###

def parse(filename):
	"""Runs the whole damn thing"""
	folders()
	make_sequential(filename)

### testing ###
# parse("distributed-computing.topic")

import os
import re
import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

directory = ''


Files = ["package.json","requirements.txt","pom.xml","build.gradle","Gemfile.lock"]
Op = open("Dependencies.txt","w")

def GemParser(file):
	f = open(directory+file,'rU')

	r = f.read()
	#::before\s+"\s([\s\W.]+)\s\(

	result = re.findall('DEPENDENCIES[\w\s.\S]*', r)

	for r in result:
		Op.write(r+"\n")

def PomParser(file):
	fr = open(directory+file,'rU')

	r = fr.read()

	soup = BeautifulSoup(r)

	links = soup.find_all("dependency")

	c = 1
	for link in links:
		Op.write(str(c) + '.   ' + link.groupid.text + ' ' + link.artifactid.text + ' ' + link.version.text + '\n' )
		#print c, link.find_all("groupId")
		c+=1

def GradleParser(file):
	f = open(directory+file,'rU')

	r = f.read()
	#::before\s+"\s([\s\W.]+)\s\(

	s = '\s*classpath\s*'

	result = re.findall('dependencies\s{([^}]*)}', r)

	for r in result:
		Op.write(r+"\n")

def JSONParser(file):
	with open(directory + file) as json_data:
	    d = json.load(json_data)
	    try:
	    	s = str(d["dependencies"])
	    	if s:
	    		Op.write("Dependencies\n")
	    		Op.write(s + '\n')
	    except:
	    	pass
	    
	    try:
	    	s = str(d["devDependencies"])
	    	if s:
	    		Op.write("devDependencies\n")
	    		Op.write(s + '\n')
	    except:
	    	pass

	    try:
	    	s = d["peerDependencies"]
	    	if s:
	    		Op.write("peerDependencies\n")
	    		Op.write(s + '\n')
	    except:
	    	pass

def Process(file,direct):
	directory = direct+'/'
	fileName = file.split('.')
	ext=''
	if(len(fileName)>1):
		ext = fileName[1]
	else:
		ext = '' 

	Op.write(directory+file+'\n')
	if(ext == 'json'):
		#Op.write("JSON Dependencies\n")
		JSONParser(file)
	elif(ext == 'txt'):
		#Op.write("Python Dependencies(.txt)\n")
		f = open(directory+file,'r')
		Op.write(f.read())
		
	elif(ext == 'gradle'):
		#Op.write("build.gradle Dependencies\n")
		GradleParser(file)
	elif(ext == 'xml'):
		#Op.write("pom.xml Dependencies\n")
		PomParser(file)
	elif(ext == 'lock'):
		#Op.write("lock Dependencies\n")
		GemParser(file)
	Op.write ("\n-----------------------------------\n")

def Scan():
	rootDir = '.'
	for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
	    #print('Found directory: %s' % dirName)
	    for fName in fileList:
			if(fName in Files):
					print dirName+'/'+fName
					Process(fName,dirName)


Scan()



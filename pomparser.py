import requests
from bs4 import BeautifulSoup

#url = "http://mvnrepository.com/artifact/org.springframework.data"
#r = requests.get(url)

fr = open("./pom.xml",'rU')

r = fr.read()

soup = BeautifulSoup(r)

links = soup.find_all("dependency")

c = 1
for link in links:
	print str(c) + '.   ' + link.groupid.text + ' ' + link.artifactid.text + ' ' + link.version.text
	#print c, link.find_all("groupId")
	c+=1
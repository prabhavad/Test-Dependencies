import re

f = open("./Gemfile.lock",'rU')

r = f.read()
#::before\s+"\s([\s\W.]+)\s\(

result = re.findall('DEPENDENCIES[\w\s.\S]*', r)

for r in result:
	print r

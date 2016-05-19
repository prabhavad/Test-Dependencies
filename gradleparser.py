import re

f = open("./build.gradle",'rU')

r = f.read()
#::before\s+"\s([\s\W.]+)\s\(

s = '\s*classpath\s*'

result = re.findall('dependencies\s{([^}]*)}', r)

for r in result:
	print r

import json
from pprint import pprint

def Parser(filename):
	with open('./package.json') as json_data:
	    d = json.load(json_data)
	    try:
	    	s = d["dependencies"]
	    	if s:
	    		print "Dependencies"
	    		print s
	    except:
	    	pass
	    
	    try:
	    	s = d["devDependencies"]
	    	if s:
	    		print "devDependencies"
	    		print s
	    except:
	    	pass

	    try:
	    	s = d["peerDependencies"]
	    	if s:
	    		print "peerDependencies"
	    		print s
	    except:
	    	pass
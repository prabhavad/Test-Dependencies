import os

def explore(direc):
	try:
		for files in os.listdir(direc):
			if '.' in files:
				print files
				c+=1
			else:
				try:
					a = os.listdir(files)
					p = os.path.join(direc,files)
					explore(p)
				except:
					print files
	except:
		pass

explore('.')
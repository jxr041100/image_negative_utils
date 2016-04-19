import os
import re

from subprocess import call
inputpath = '/home/goddess/data/car/neg'
filename_prefix ='non_car'



alist_filter = ['jpg','bmp','png']


f = open(filename_prefix+'.dat','w')
for dirpath, dirs, files in os.walk(inputpath):	
	for filename in files:
		if filename[-3:] in alist_filter
			fullpath = os.path.join(dirpath,filename) 
			print "full path" +fullpath

			printstr = fullpath			
			printstr += '\n'
			#write to the info file
			print printstr			
			f.write(printstr)			
f.close()

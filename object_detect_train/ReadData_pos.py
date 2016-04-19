import os
import re
#mport imghdr
#import struct

import Image
from subprocess import call
inputpath = '/home/jeff/data/car/pos'
filename_prefix ='car'

def get_image_size(fname):
	IM=Image.open(fname)
	width,height=IM.size
	return width, height

alist_filter = ['jpg','bmp','png']


f = open(filename_prefix+'.dat','w')
for dirpath, dirs, files in os.walk(inputpath):	
	for filename in files:
		if filename[-3:] in alist_filter:
			fullpath = os.path.join(dirpath,filename) 
			print "full path" +fullpath

			printstr = fullpath
			w, h = get_image_size(fullpath)
			printstr += " 1 0 0"
			printstr += " "+str(w)+ " "+str(h)+"\n"
			#write to the info file
			print printstr			
			f.write(printstr)
	#close the file			
f.close()

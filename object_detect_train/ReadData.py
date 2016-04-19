import os
import re
#mport imghdr
#import struct

import Image
from subprocess import call
inputpath = '/home/goddess/SKY/skyHub/ObjectDetect_CSIM/Training/data/CarData/neg'
filename_prefix ='neg'

# def get_image_size(fname):
#     '''Determine the image type of fhandle and return its size.
#     from draco'''
#     with open(fname, 'rb') as fhandle:
#         head = fhandle.read(24)
#         if len(head) != 24:
#             return
#         if imghdr.what(fname) == 'png':
#             check = struct.unpack('>i', head[4:8])[0]
#             if check != 0x0d0a1a0a:
#                 return
#             width, height = struct.unpack('>ii', head[16:24])
#         elif imghdr.what(fname) == 'gif':
#             width, height = struct.unpack('<HH', head[6:10])
#         elif imghdr.what(fname) == 'jpeg':
#             try:
#                 fhandle.seek(0) # Read 0xff next
#                 size = 2
#                 ftype = 0
#                 while not 0xc0 <= ftype <= 0xcf:
#                     fhandle.seek(size, 1)
#                     byte = fhandle.read(1)
#                     while ord(byte) == 0xff:
#                         byte = fhandle.read(1)
#                     ftype = ord(byte)
#                     size = struct.unpack('>H', fhandle.read(2))[0] - 2
#                 # We are at a SOFn block
#                 fhandle.seek(1, 1)  # Skip `precision' byte.
#                 height, width = struct.unpack('>HH', fhandle.read(4))
#             except Exception: #IGNORE:W0703
#                 return
#         else:
#             return
#         print str(width) +" "+ str(height)
#         return width, height

def get_image_size(fname):
	IM=Image.open(fname)
	width,height=IM.size
	return width, height

f = open(filename_prefix+'.inf','w')
for dirpath, dirs, files in os.walk(inputpath):	
	for filename in files:
		print filename
		srchobj = re.match(r'neg',filename)
		if srchobj:
			#full path/filename 1, 0, 0 width length
			#read the full path of the file			
			fullpath = os.path.join(dirpath,filename) 
			print "full path" +fullpath

			printstr = fullpath 
			
			if filename_prefix == "pos":
				#width and heigth
				printstr += " 1 0 0"
				try: 
					w, h = get_image_size(fullpath)
					printstr += " "+str(w)+ " "+str(h)+"\n"
				except:
					print "not a supported image"
					continue
			else:
				printstr += '\n'
			#write to the info file
			print printstr
			#raw_input("write")
			f.write(printstr)
#close the file			
f.close()
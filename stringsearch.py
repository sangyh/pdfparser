#from docx import *
import zipfile
import os

src_dir='./'

for file in os.listdir(src_dir):
	content=open(file,"r")

	# if file.endswith("docx"):
	# 	z=zipfile.ZipFile(file)
	# 	for word in z.read("word/document.xml"):
	# 		print(word)

	#else:
	for line in content:
		print (line)




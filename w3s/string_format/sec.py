import xml.dom.minidom as MD
import sys
import zipfile

__author__ = "Pablo Castellano <pablo@anche.no>"
__license__ = "GNU GPLv3+"
__version__ = 0.2
__date__ = "14/04/2012"

TEXT_FILE = "D:/7/word/document.xml"

print ("Recover corrupted Word 2006 files")
print ("Copyright (C) 2012 Pablo Castellano")
print ("This program comes with ABSOLUTELY NO WARRANTY.")
print ("This is free software, and you are welcome to redistribute it under certain conditions.")
print

if len(sys.argv) != 2:
	print("Usage: %s <corrupted_file.doc>" %sys.argv[0])
	sys.exit(1)

f = zipfile.ZipFile(sys.argv[1])
s = f.read(TEXT_FILE)
f.close()

#Save for debug
#fp = open("document.xml", "w")
#fp.write(s)
#fp.close()

#tree = MD.parse(filename)
tree = MD.parseString(s)
nodes = tree.getElementsByTagName("w:t")

fp = open("document.txt", "w")

for i in nodes:
	s = i.childNodes[0].nodeValue.encode('utf-8') + '\n'
	fp.write(s)

fp.close()

print ("I hope you got something useful in document.txt")
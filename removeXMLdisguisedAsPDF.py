#Script to go through a directory of files and remove every
#file that has a .pdf extension but is actually xml 
#Decision based on first line in file == XML header
import os
from os.path import basename

path = raw_input('Please provide path to directory: ')
if not len(path)<1:
	os.chdir(path)

wd = os.getcwd()
entries = os.listdir(wd)
print len(entries)

for entry in os.listdir(wd):
	if os.path.isfile(entry):
		fparts = os.path.splitext(basename(entry))
		ext = fparts[1]        
		
		if not ext.lower() == '.pdf':
			print 'Skipping file',entry
			continue   
			
		with open(entry, 'r') as f:
			txt = f.readline().strip()
			#print txt, entry
			if txt.startswith('<?xml version'):
				try:
					f.close()
					os.remove(entry)
					print 'Removed file', entry
				except OSError, e:
					print ("Error: %s - %s." % (e.filename,e.strerror))
			#else:
			#	print 'File seems to be pdf:', entry
				
print 'Removed', len(entries)-len(os.listdir(wd)), 'files'
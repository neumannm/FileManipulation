#Script for renaming all files in a directory
#new file names have a common format - same length, random capital letters and numbers
#changes are logged in text file
import os
from os.path import basename
import string
import random

def generateRandomName(ext, size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))+ext

path = raw_input('Please provide path to directory: ')
if not len(path)<1:
    os.chdir(path)

wd = os.getcwd()

output = open('changes.txt', 'w')
output.write('New Name\tOld Name\n')

for entry in os.listdir(wd):
    if os.path.isfile(entry):
        fparts = os.path.splitext(basename(entry))
        ext = fparts[1]        
        
        if not ext.lower() == '.pdf':
            print 'Skipping file',entry
            continue       
        
        newName = generateRandomName(ext)
        
        os.rename(entry, newName)
        output.write(newName)
        output.write('\t')
        output.write(entry)
        output.write('\n')

output.close()

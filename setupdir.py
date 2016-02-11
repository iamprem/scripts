#!/usr/bin/env python


import zipfile as z
import gzip, tarfile
import os,sys
import re

# Check & Create directory for extracted files
cwd = os.getcwd()
source = cwd + '/hw1_test'
target = cwd + '/py_extracted'
if not os.path.exists(source):
    sys.exit('Source folder *hw1_test* doesn\'t exist')
if not os.path.exists(target):
    os.makedirs(target)

# Submission Info

zipnames = os.listdir(source)
submitcount = len(zipnames)

for zipfile in zipnames:
    namepattern = re.compile('(([A-Za-z ])+)?')
    formatpattern = re.compile('\.[a-zA-Z0-9]+$')
    fileformat = formatpattern.search(zipfile).group()
    match = namepattern.match(zipfile)
    dirname = match.group()
    extractpath = target + '/' + dirname
    if fileformat == '.zip':
        z.ZipFile(source + '/' + zipfile).extractall(extractpath)
    elif fileformat == '.tar':
        tarfile.TarFile(source + '/' + zipfile).extractall(extractpath)
    elif fileformat == '.gz':
        os.system('mkdir -p '+extractpath.replace(' ','\ ')+' && tar -xzf '+source.replace(' ', '\ ') + '/' + zipfile.replace(' ','\ ') +' -C '+extractpath.replace(' ', '\ '))
    elif fileformat == '.7z':
        os.system('7zr e '+source.replace(' ', '\ ') + '/' + zipfile.replace(' ','\ ') +' -o'+extractpath.replace(' ', '\ '))
    else:
        print('NOT A ZIP FILE')

if len(os.listdir(target)) == submitcount:
    print('All Folders are extracted')
else:
    print('NOT ALL FOLDERS ARE EXTRACTED')
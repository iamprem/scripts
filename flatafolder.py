import shutil
import os

# copy all the files in the subfolders to main folder

# Go to extracted directory
hw_dir = os.getcwd() + '/' + 'py_extracted'
studentdirs = os.listdir(hw_dir)

for student in studentdirs:
    studentdir = hw_dir +'/'+student
    for root, dirs, files in os.walk(studentdir, topdown=False):
        for name in files:
            shutil.move(root+'/'+name, studentdir+'/'+name)
        for name in dirs:
            print 'Deleting '+root+'/'+name
            os.rmdir(root+'/'+name)
        print 'CLEARED: '+root

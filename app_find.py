import os
import sys
import subprocess
import re

from subprocess import Popen, PIPE

fname = sys.argv[1]

file = open(fname, 'r')
data = file.readlines()


search_str = 'Successfully signed: C' 
search_str2 = 'Successfully signed and timestamped: C:'

buff = []

for line in data:
	if search_str in line or search_str2 in line:
		#y= line.find('Release')
		#print line.split()[-1]
		x = line.split()[-1]
		#print x
		#x = line[y+8:]
		#print os.path.basename(x), os.path.dirname(x)
		z= os.path.basename(x)
		# print z

		buff.append(z)

#print buff
for item in set(buff):
	print item

	


# for line in data:
# 	if line.find('successfully') >= 0 and line.find('Release') >= 0:
# 		print line.split()[-1]



# for line in data:
# 	x = re.search(search_str, line)
# 	if x:
# 		#print line.split()[-1]
# 		x = line.split()[-1]
# 		print os.path.basename(x), os.path.dirname(x)


# def run_command(cmd):
#     process = Popen([cmd], stdout=PIPE, stderr=PIPE, shell=True)
#     stdout, stderr = process.communicate()
#     return stdout


#cmd1 = "grep 'successfully signed in binary bit' /home/binit/Documents/python_code/file7.txt | awk '{print $NF}'"

## cmd1 = "grep 'successfully signed in binary bit' %s %s| awk '{print $NF}'" %(fname, uname)
#cmd1 = "grep 'successfully signed in binary bit' {} {} | awk '{print $NF}'".format(fname, uname)

## cmd1 = "grep 'successfully signed in binary bit' %s | awk '{print $NF}'" %fname
# cmd1 = """grep 'successfully signed in binary bit' %s | awk '{print $NF}'""" %(fname)
# print cmd1





# grep 'successfully signed in binary bit' file7.txt | awk '{print $NF}'
# grep 'successfully signed in binary bit' file7.txt | awk -F/ '{print $NF}'
# grep 'successfully signed in binary bit' file7.txt | awk -F. '{print $NF}'
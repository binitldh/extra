import os
import sys

fname = sys.argv[1]

file = open(fname, 'r')

data = file.readlines()
v = set(data)

for item in data:
	print item
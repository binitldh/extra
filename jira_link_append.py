import os
import sys

fname = sys.argv[1]
fname2 = sys.argv[2]

file = open(fname, 'r')
file2 = open(fname2, 'w')

for line in file:
	if ("[TE-") in line:
		#print line
		x = line.find('[TE-')
		y = line.find(']')
		z = line[x:y+1]
		z1 = line[x+1:y]
		print z, z1
		s = line.replace(z, '<a href="https://tallyjira.tallysolutions.com/browse/{}" target="_blank">[{}] </a>'.format(z1, z1))
		file2.write(s)

	else:
		file2.write(line)

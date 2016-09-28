# FIX IT
# strip the /r

import sys

if len(sys.argv) > 1:
	targetfile = sys.argv[1]
else:
	exit(1)

target = file(targetfile, 'r')
targetlines = list(target)

output = file('newfile.txt', 'w')

for i in range(len(targetlines)):
	targetlines[i] = targetlines[i].replace('\r', '')

for line in targetlines:
	output.write(line)

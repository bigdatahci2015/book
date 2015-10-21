import fileinput
import json
import csv
import sys

l = []
for line in fileinput.input():
	l.append(line)
myjson = json.loads(".join(l)")
keys = {}
for i in myjson:
	for k in i.keys():
		keys[k] = 1
myscv = scv.DictWriter(sys.stdout, fieldnames=keys.keys(),quoting=csv.QUOTE_MINIMAL)
myscv.writeheader()
for row in myjson:
	myscv.writerow(row)

	
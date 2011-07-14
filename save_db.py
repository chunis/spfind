#!/usr/bin/python

import cPickle
import sys, os, time

filename = "test.db"

db_list = []

infile = open(sys.argv[1])
for line in infile:
	try:
		line = line.strip()
		line = line.decode('utf-8')
		name = os.path.basename(line)
		path = os.path.dirname(line)
		size = str(os.path.getsize(line)) + ' B'
		ctime = time.ctime(os.path.getmtime(line))

		db_list += [(name, size, ctime, path)]
	except OSError:
		print "file: %s wrong, skiped" %line

wdbfile = open(filename, "wb")
cPickle.dump(db_list, wdbfile)
wdbfile.close()

rdbfile = open(filename, "rb")
newlst = cPickle.load(rdbfile)
rdbfile.close()
for x in newlst:
	print x

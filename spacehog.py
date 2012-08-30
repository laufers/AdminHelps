#!/usr/local/epd/bin/python

import subprocess
import argparse
import glob
import datetime as dtg


parser = argparse.ArgumentParser(description='Check space of users and look for hogs.')
parser.add_argument('dirname', metavar='DIRNAME', type=str, default='.', nargs='?', 
                    help='Directory path and glob for searching. Needs to be in quotes.')
parser.add_argument('--sizelimit','-s', dest='sizeLimit', type=int, default= 500,
                    help='Size threshold in megaabytes (MB)')
parser.add_argument('--log','-l', action = 'store_true',
                    help='Saves output to a log file.')
args = parser.parse_args()

# print args.dirname, args.sizeLimit

files = glob.glob(args.dirname)
sizeLimit = args.sizeLimit * 1024 
 

users = subprocess.check_output(["du", "-sk"] + files)

# split string into lines
splithogs = [s.split("\t", 1) for s in users.splitlines()]

#split lines into data
splithogs = [(int(s[0]), s[1]) for s in splithogs if int(s[0]) > sizeLimit]

splithogs.sort(reverse = True)

date_string = dtg.datetime.now().strftime("%Y%m%d%H")
if args.log:
	fn = 'space.' + date_string + '.log'
	f = open(fn, 'w')

for size,dirName in splithogs:
	print '%d MB \t: %s' % (size/1024, dirName)
	if args.log:
		f.write('%d MB \t: %s\n' % (size/1024, dirName))

if args.log:
	f.close()
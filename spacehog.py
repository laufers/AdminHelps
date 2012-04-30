#!/usr/local/epd/bin/python

import subprocess
import argparse
import glob

# check argument for directory else default to current directory

# if len(sys.argv) < 2:
#     dirname = "." 
# else:
#     dirname = sys.argv[1]

parser = argparse.ArgumentParser(description='Check space of users and look for hogs.')
parser.add_argument('dirname', metavar='DIRNAME', type=str, default='.', nargs='?', 
                    help='Directory path and glob for searching. Needs to be in quotes.')
parser.add_argument('--sizelimit','-l', dest='sizeLimit', type=int, default= 500,
                    help='size threshold in megaabytes (MB)')
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

for size,dirName in splithogs:
	print '%d MB \t: %s' % (size/1024, dirName)

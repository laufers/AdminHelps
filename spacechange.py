#!/usr/bin/python

import subprocess
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Compare output from spacehog.py from two space checks and compute the percent change.')
parser.add_argument('file1', type=str, help='Newer file of users space usage', nargs =1)
parser.add_argument('file2', type=str, help='Older file of users space usage', nargs =1)

args = parser.parse_args()

nlist = open(args.file1[0], 'r')
olist = open(args.file2[0], 'r')

current = np.genfromtxt(nlist, dtype = None, names=['space','junk','junk', 'user'])

last = np.genfromtxt(olist, dtype = None, names=['space','junk','junk', 'user'])

# cc = 0
# for user in current['user']:
# 	cl = 0
# 	if user  in  last['user']:
# 		print '========='
# 		print 'current: ', user, current['space'][cc], cc 
# 		print 'last:    ', last['user'][cl], last['space'][cl], cl
# 		percentChange = 100 * (float(current['space'][cc]) - float(last['space'][cl])) / float(last['space'][cl])
# 		print percentChange
# 		cl = cl + 1
# 	else:
# 		print '********'
# 		print user, ' is a new user to the spacehog list.'
# 	cc = cc + 1

for row in current:
	lastrow =  last[last['user'] == row['user']]
	print float(100. * (lastrow['space'].astype(np.float) - row['space'])/row['space']), row['user'] 

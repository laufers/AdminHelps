#!/usr/bin/env python

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

for row in current:
	if row['user'] in last['user']:
		lastrow =  last[last['user'] == row['user']]
		percentChange =  round(float(100. * (row['space'] - lastrow['space'].astype(np.float))/lastrow['space']), 2)
		if percentChange != 0.0:
			User = row['user'].split( '/')
#			print User[2],'   \t', percentChange,  "% change.", lastrow['space'].squeeze(), "MB"  
			print "%s      \t %.2f%% change.  \t current: %i MB \t old: %i MB "  %(User[2], percentChange, row['space'].squeeze(), lastrow['space'].squeeze())

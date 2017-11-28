#!/usr/bin/env python
from __future__ import division
import mincemeat
import sys


# Don't forget to start a client!
# ./mincemeat.py -l -p changeme
f = open(sys.argv[1],"r")
data = list(f)
f.close()
#file = open('test.txt','r')
#data = list(file)
#file.close()


# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    for word in v.split():
		word = word.strip().lower()
		for char in word:
			yield char,1
			yield 'char_count',1
		
		
      

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

resultlist = []
total=results.get('char_count')

for k in results.keys():
  resultlist.append((k,results[k]))
  
resultlist = sorted(resultlist, key=lambda a:a[1])

#print resultlist
#print total

for k,v in resultlist:
	
	per=(v*100/total)
	if k != 'char_count':
		print k,v,"%0.1f" % per,"%"
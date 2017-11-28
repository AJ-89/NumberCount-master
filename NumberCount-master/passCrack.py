import sys
import md5
import hashlib
import mincemeat
import itertools

enumdata=[]
datasource={}
hash = sys.argv[1]
print 'Attacking '+hash


def mapfn(k,v):
 list={}
 import md5
 val=v.split()
 subString=val[-1]
 for list in val:
   list=list.strip()
   
   hashedString=md5.new(list).hexdigest()
   if hashedString[:5]==subString:
     yield list,subString

def reducefn(k,vs):
	return vs

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2','3','4','5','6','7','8','9']
all=[]
all=alphabets + numbers
for r in range(1, 5):
    for s in itertools.product(all, repeat=r):
           vallue = ''.join(s)
           enumdata.append(vallue)
	       

temp = ''
counter = 0


for line in enumdata:
  temp = temp + line.rstrip() + ' '
  if counter % 1000 == 0:
    temp = temp + hash
    datasource[counter] = temp
    temp = ''
  counter += 1
  
datasource[counter] = temp

s=mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn =reducefn

results = s.run_server(password="changeme")
print results.keys()


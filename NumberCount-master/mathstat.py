from __future__ import division
import mincemeat
import sys
import math

file=open(sys.argv[1],'r')
data=list(file)
file.close()

array=[]
temp=[]

count=0
for num in data:
   count= count+ 1
   temp.append(int(num.rstrip('\n')))
   if((count%10)==0):
       array.append(temp)
       temp=[]
array.append(temp)

datasource=dict(enumerate(array))





def mapfn(k,v):
    for num in v:
        yield 'sum',num
       
    

def reducefn(k,v):
    total=sum(v)
    n=len(v)
    mean=float(total)/n
    stddev=0
    for num in v:
		stddev= (pow(abs(num-mean),2)) + stddev  
		
    std_deviation=pow((stddev/n),0.5)
    return n,total,std_deviation

s=mincemeat.Server()
s.datasource=datasource
s.mapfn=mapfn
s.reducefn=reducefn

results=s.run_server(password="changeme")

reslist=[]

print 'Count,Sum, Standard Deviation : ',results['sum']



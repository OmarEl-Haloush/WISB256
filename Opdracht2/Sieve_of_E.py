import time
import sys
import math
# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
T1=time.perf_counter()
N=sys.argv[1]
file=sys.argv[2]
n=int(N)
string=list(range(2,int(N)+1))
x=2
i=2
j=i 
string
while i <=math.sqrt(n):
    #if i in string: 
    if i>=10 and j>=1000:
        i+=1
        j=i
    if i*j in string:
        p=i*j
        string.remove(p)
        #if p-1>0 and p-1<len(string):
         #   fout=open(sys.argv[2],'w')
          #  fout.write(str(string[p-1])+'\n')
            #fout.write('\n')
           # fout.close()
        j+=1    
    elif i*j<=n:
        j+=1
    else:
        i+=1
        j=i
        
#fout=open(sys.argv[2],'w')
#i=0
#for i in string:
 #   fout.write(str(i))
 #   fout.write('\n')
 

T2=time.perf_counter()
print('Time required to find',len(string),'in',T2-T1,'sec.')
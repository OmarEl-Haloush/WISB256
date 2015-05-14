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
string=[]
x=2
while x <=n:
    string.append(x)
    x+=1
for i in string:
    j=i
    
    if i*j<=n and i<=math.sqrt(n):
        p=i*j
        if p in string:
            string.remove(p)
            
        j+=1
    else:
        i+=1
fout=open(sys.argv[2],'w')
i=0
for i in string:
    fout.write(str(i))
    fout.write('\n')
 
fout.close()
T2=time.perf_counter()
print('Time required to find',len(string),'in',T2-T1,'sec.')
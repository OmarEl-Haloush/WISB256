import time
import sys
import math
# initialize the 
T1=time.perf_counter()
N=int(sys.argv[1])
PrimeList= list(range(0,N))
PrimeList[1] =0
# loop
for i in range(1,int(math.sqrt(N))):
    if PrimeList[i] !=0:
        for j in range(i*i,N,i):
            PrimeList[j]=0
PrimeList1=list()   
fout=open(sys.argv[2],'w')
for z in PrimeList:
    if z>0:
        PrimeList1.append(z)
        fout.write(str(z))
        fout.write('\n')
        
'''while PrimeList[z]<(len(PrimeList)-1):
    print(PrimeList[z])
    print(PrimeList[z],len(PrimeList),z)
    if PrimeList[z]==0:
        PrimeList.remove(0)
    z+=1    '''

T2=time.perf_counter()        
print('Time required to find',len(PrimeList1),'in',T2-T1,'sec.')

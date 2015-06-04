import random
import math
import sys
# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
if len(sys.argv) <3:
    print('Use: estimate_pi.py N L')
elif float(sys.argv[2])>1:
    print('AssertionError: L should be smaller than 1')
else:
    N=int(sys.argv[1])
    L=float(sys.argv[2])
    h=0
    def dropneedle(L):
        x=random.random()
        y=random.random()
        a=random.vonmisesvariate(0,0)
        endpoint1=x+L*math.cos(a)
        x1=int(x)
        L1=math.floor(endpoint1)
        endpoint2=y+L*math.sin(a) 
        y1=int(y)
        L2=int(endpoint2)
        if L1==1 or L1==-1:# or y1>=1 or L2>=1:
            return True
        else:
            return False
    if len(sys.argv)>3:
        if float(sys.argv[3])>=0:
            random.seed(int(sys.argv[3]))
        
    while N>0:
        if dropneedle(L)==True:
            h+=1
            N-=1
        else:
            N-=1
    '''if N==0 and h>0:'''
    Pi=(float(sys.argv[1])*2*float(sys.argv[2]))/max(1, h)
    print(h,'hits in',sys.argv[1],'tries')
    print('Pi =',Pi)
        
        
        
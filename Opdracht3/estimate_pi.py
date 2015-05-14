import random
import math
import sys
# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
N=int(sys.argv[1])
L=int(sys.argv[2])
Seed=int(sys.argv[3])
h=0
p=False
if len(sys.argv) <=3:
    print('Use: estimate_pi.py N L Seed')
elif L>1:
    print('AssertionError: L should be smaller than 1')
else:
    def dropneedle(L):
        p=False
        #random.seed(Seed)
        x=random.random()
        y=random.random()
        a=random.vonmisesvariate(0,0)
        print(x,y,a)
        endpoint1=x+L*math.cos(a)
        endpoint2=y+L*math.sin(a)
        print(endpoint1,endpoint2)
        if endpoint1>=0:
            return False 
        elif  endpoint2<=0:
            return False
        else:
            return True
    while N>0:
        if dropneedle(L)==True:
            h+=1
            print(h,N)
            N-=1
        else:
            N-=1
    print(p,N,h)        
    if N==0 and h>0:
        Pi=int(sys.argv[1])/h
        print(h,' hits in ', sys.argv[1], 'Tries')
        print('Pi= ', Pi)
        
        
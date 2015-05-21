import random
import math
import sys
# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
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
        endpoint2=y+L*math.sin(a)
        if endpoint1<=((2*L)/math.pi):
            return True
        elif  endpoint2>=((2*L)/math.pi):
            return True
        else:
            return False
    while N>0:
        try:
            if float(sys.argv[3])>=0:
                random.seed(sys.argv[3])
                if dropneedle(L)==True:
                    h+=1
                    N-=1
                else:
                    N-=1
        except:
            if dropneedle(L)==True:
                h+=1
                N-=1
            else:
                N-=1
    if N==0 and h>0:
        Pi=(2*L*int(sys.argv[1]))/h
        print(h,' hits in ', sys.argv[1], 'Tries')
        print('Pi= ', Pi)
        
        
        
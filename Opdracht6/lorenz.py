import math
import random
from scipy import integrate
import numpy
#from scipy import integrate
#from numpy import arrange

class Lorenz:
    #def __slots__(self):
     #   ('_initial','_sigma','_rho','_beta')
    def __init__(self,initial,sigma=10,rho=10,beta=10):
        self.initial=initial
        self.sigma=sigma
        self.rho=rho
        self.beta=beta
        self.x=self.initial[0]
        self.y=self.initial[1]
        self.z=self.initial[2]
        x=initial[0]
        y=initial[1]
        z=initial[2]
        self.funcy=(x*(rho-z-y))
        self.funcx=(sigma*(y-x))
        self.funcz=((x*y)-beta*z)
        return
    def __str__(self):
        new1=str()
        for i in self.initial:
            new=i
            new1+=str(new)
            new1+=(str(' '))
        return str((new1)+'\n'+"{:.6f}".format(self.sigma)+'\n'+"{:.6f}".format(self.rho)+'\n'+"{:.6f}".format(self.beta)+'\n')
    def function(self):
        
        xinit=[0,0]
        yinit=[0,0]
        zinit=[0,0]
        
        x=(x*(self.rho-z-y))
        y=(self.sigma*(y-x))
        z=((x*y)-self.beta*z)
       
        #print(x1_0,y1_0,z1_0)
        #return x1_0,y1_0,z1_0
        return (x,y,z)    
    def solve(self,T=100,dt=0.02):
        Tmax=numpy.arange(0,T,dt)
        print(Tmax)
        opl=integrate(self.function(),self.initial,Tmax)
        print(opl)
        return opl
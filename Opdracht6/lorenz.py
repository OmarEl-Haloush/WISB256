import math
import random
from scipy.integrate import odeint
import numpy
#from scipy import integrate
#from numpy import arrange

class Lorenz:
    #def __slots__(self):
     #   ('_initial','_sigma','_rho','_beta')
    def __init__(self,initial,sigma=10,rho=28,beta=8/3):
        self.sigma=sigma
        self.rho=rho
        self.beta=beta
        self.xyz=initial
        return
    def __str__(self):
        new1=str()
        for i in self.xyz:
            new=i
            new1+=str(new)
            new1+=(str(' '))
        return str((new1)+'\n'+"{:.6f}".format(self.sigma)+'\n'+"{:.6f}".format(self.rho)+'\n'+"{:.6f}".format(self.beta)+'\n')
    def function(self,xyz,t):
        q=[0,0,0]
        q[0]=(self.sigma*(xyz[1]-xyz[0]))
        q[1]=(xyz[0]*(self.rho-xyz[2]-xyz[1]))
        q[2]=((xyz[0]*xyz[1])-self.beta*xyz[2])
        #print(x1_0,y1_0,z1_0)
        #return x1_0,y1_0,z1_0
        xyz=q
        return q
        
    def solve(self,T,dt):
        Tmax=numpy.arange(0,T,dt)
        opl1=list
        opl=(odeint(self.function,self.xyz,Tmax))
        
        return opl
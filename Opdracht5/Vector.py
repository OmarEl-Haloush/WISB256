import math
class Vector:
    ''' Rationeel getal
    eigenschappen: (teller(int), noemer(int))
    '''
    def selfv(self):
        ('_v1','_v2','_v3')
    
    def __init__(self,n,v=[0]):
        i=0
        
        if isinstance(v,int) or isinstance(v,float):
            v=[float(v)]
            
            while (len(v))<n:
                v.append(v[len(v)-1])
        elif isinstance(v,list):
            while (len(v))<n:
                v.append(0)
        #while i<=len(v)-1:
        new=list()
        for i in v:
            new.append(i)
            #i+=1
        
        self.v=list()
        self.v=new
        return
    def __str__(self):
        new1=str()
        new=list(self.v)
        for i in new:
            new1+=(str("{:.6f}".format(float(i))+'\n')) #str("{:.6f}".format(self))
        return str(new1)
    def lincomb(self,other,alpha,beta):    
        new=Vector(len(self.v))
        new.v=list()
        i=0
        while len(new.v)<len(self.v):
            new.v.append((self.v[i]*alpha)+(other.v[i]*beta))
            i+=1
        return new 
    def scalar(self,alpha):
        new=Vector(len(self.v))
        new.v=list()
        i=0
        while len(new.v)<len(self.v):
            new.v.append((self.v[i]*alpha))
            i+=1
        return new
    def inner(self,other):
        new=0
        i=0
        while i<len(self.v):
            new+=((self.v[i]*other.v[i]))
            i+=1
        return new
    def norm(self):    
        other=self
        new=math.sqrt(self.inner(other))
        return new    
       
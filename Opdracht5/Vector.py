import math
class Vector:
    ''' Rationeel getal
    eigenschappen: (teller(int), noemer(int))
    '''
    #def __slots__(self):
     #   ('_v1','_v2','_v3')
    
    def __init__(self,n,v=[0,0,0]):
        if isinstance(v,int) or isinstance(v,float):
            v=[v]
        while len(v)<3:
            if v[0]==0:
                v+=[0]
            else:
                bier=len(v)-1
                v+=[v[bier]]
            
        self.v1=v[0]
        self.v2=v[1]
        self.v3=v[2]    
        '''if v[0]>=0 and v[1]==0:
            self.v1=v[0]
            self.v2=v[0]
            self.v3=v[0]
        elif v[0]>0 and v[1]>0 and v[2]==0:
            self.v1=v[0]
            self.v2=v[1]
            self.v3=v[1]
        elif v[0]>0 and v[1]>0 and v[2]>0:
            self.v1=v[0]
            self.v2=v[1]
            self.v3=v[2]
        else:
            print('Error: Use Vector(n,v1,v2,v3): v(max)==3')'''
            
    def __str__(self):
        return str("{:.6f}".format(self.v1))+'\n'+str("{:.6f}".format(self.v2))+'\n'+str("{:.6f}".format(self.v3))
    def lincomb(self,other,alpha,beta):    
        new=Vector(3)
        new.v1=((self.v1*alpha)+(other.v1*beta)) 
        new.v2=((self.v2*alpha)+(other.v2*beta))
        new.v3=((self.v3*alpha)+(other.v3*beta))
        return new
    def scalar(self,alpha):
        new=Vector(3)
        new.v1=(self.v1*alpha)
        new.v2=(self.v2*alpha)
        new.v3=(self.v3*alpha)
        return new

    def inner(self,other):
        new=(self.v1*other.v1+self.v2*other.v2+self.v3*other.v3)
        return new
    def norm(self):
        other=self
        new=math.sqrt(self.inner(other))
        return new    
        











''''from array import array
u=array('d',[1,3,4])
v=array('d',[2,1,3])
w=u+v
print(w)
w1=array('d',[0,0,0])
for i in range(len(v)):
    w[i]=u[i]+v[i]
    print(w[i],u[i],v[i])
print(w1) '''   
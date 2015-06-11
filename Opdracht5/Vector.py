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
    def minus(self,other):
        new=Vector(len(self.v))
        new.v=list()
        i=0
        while len(new.v)<len(self.v):
            new.v.append((self.v[i]-other.v[i]))
            i+=1
        return new
def GrammSchmidt(k):
    kn=list()
    u1=k[0]
    def proju(u,v):
        proju1=v.inner(u)
        proju2=u.inner(u)
        proju3=(proju1/proju2)
        proju4=u.scalar(proju3)
        return proju4
    def un(other,proju):
        u2=other.minus(proju)
        return u2    
    for i in range(0,len(k)):
        t=k[i]
        for j in range(0,i):
            t=un(t, proju(kn[j], t))
        kn.append(t.scalar(1/(t.norm())))
    '''i=0
    while len(kn)<len(k):
            if i==0:
                new=Vector(len(k[0].v))
                new.v=list()
                while i<len(k[0].v):
                    new.v.append((k[0].v[i]))
                    i+=1
                i=1
                kn.append(new)
            else:
                
                new2=Vector(len(k[0].v))
                newl=list()
                newl.append((un(k[i],proju(k[i-1],k[i]))))
                j=2
                while j<(len(k)):    
                    newl.append((proju(k[j-1],k[j])))
                    j+=1
                md=list()
                print(newl[len(newl)-1],newl[len(newl)-1].v)
                #print(newl[0],newl[1])
                while len(newl)>1:
                    md+=(newl[len(newl)-2].minus(newl[len(newl)-1]))
                    newl.pop(len(newl)-1)
                newl.append(md)    
                kn.append(newl)    
                i+=1
                #new=Vector(len(k[0].v))
                #new.v=list()
                #print(new.v)
                #kn.append(new)
    #print(u1)
    #print(k[1])
    #print(u2)
    #print('Grammy')
    #print(k[0],len(k[0].v))
    #print(new)
    j=0
    i=0
    kn1=list()
    while j<len(kn):
        plen=len(kn[j].v)
        new=Vector(len(kn[j].v))
        new.v=list()
        while i<plen:
            new.v.append(kn[j].v[i]/kn[j].norm())
            i+=1
        j+=1
        i=0
        kn1.append(new)''' 
    return kn
        
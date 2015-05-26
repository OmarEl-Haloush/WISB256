import math
# f(x):
 #   f=x-1
  #  return f
def findRoot(f,a,b,epsilon):
    
    m=(a+b)/2
    b=float(b)
    a=float(a)
    epsilon=float(epsilon)
    #if int((a+b)/2)
    #if f(a)>0 and f(b)<0:
     #   print('No root found')
      #  return False
    if (b-a)<=epsilon:
        print('Error')
        return m
    elif abs(f(a))<(epsilon*2):
        print('Found root=',"{:.2f}".format(a))
        return a
    elif abs(f(b))<(epsilon*2):
        print('Found root=',"{:.2f}".format(b))
        return b
    elif f(a)<0.0 and f(m)>0.0:
        return findRoot(f,a,m,epsilon)
    elif f(b)<0.0 and f(m)>0.0: 
        return findRoot(f,m,b,epsilon)
    elif f(a)>0.0 and f(m)<0.0:
        return findRoot(f,a,m,epsilon)
    elif f(b)>0.0 and f(m)<0.0: 
        return findRoot(f,m,b,epsilon)    
    else:
        print('No root found(2)')

'''root=findRoot(lambda x:x-1,0,10,0.1) 
print(root)
print(findRoot(lambda x:x-1,0,10,0.1))'''
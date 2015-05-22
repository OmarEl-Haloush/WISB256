import math
# f(x):
 #   f=x-1
  #  return f
def findRoot(f,a,b,epsilon):
    
    m=int((a+b)/2)
    b=float(b)
    a=float(a)
    epsilon=float(epsilon)
    print(f(a),f(b))
    #if int((a+b)/2)
    #if f(a)>0 and f(b)<0:
     #   print('No root found')
      #  return False
    if (b-a)<=epsilon:
        print('Error')
        return m
    elif f(a)<0.0:
        findRoot(f,a,m,epsilon)
    elif f(b)<0.0: 
        findRoot(f,m,b,epsilon)
    elif f(a)==0:
        print('Found root=',a)
        return a
    elif f(b)==0:
        print('Found root=',b)
        return b
    else:
        print('No root found(2)')

#root=findRoot(lambda x:x-1,0,3,0.1) 
#print(root)
#print(findRoot(lambda x:x-1,0,3,0.1))
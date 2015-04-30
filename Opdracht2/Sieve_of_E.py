import time

#N=input('Compute all Prime numbers <N\nN= ')
N=100000
T1=time.perf_counter()
n=int(N)
string=[]
x=2
while x <=n:
    string.append(x)
    x+=1
for i in string:
    j=i
    while i in string:
        if i*j<=n:
            p=i*j
            if p in string:
                string.remove(p)
            j+=1
        else:
            i+=1
fout=open('prime.dat','w')
i=0
for i in string:
    fout.write(str(i))
    fout.write('\n')
fout.close()
T2=time.perf_counter()
print('Found',len(string),'Prime numbers smaller than',N,'in',T2-T1,'sec.')
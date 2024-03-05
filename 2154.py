f=open('27-Kb.txt')
n=int(f.readline())
a=[int(i) for i in f]
#print(a)
q=[]
s=k10=0
ms= -10**20

for i in range(4):
    s+=a[i]
    if a[i]<0 and a[i]%10 == 0:
        k10 += 1
    q.append([s,k10])
    
m=[10**20]*3


for i in range(4,n):
    s += a[i]
    if a[i] < 0 and a[i]%10 == 0:
        k10 += 1
        
    if k10!=0:
        if k10%3 == 0:
            ms = max(ms,s)
        s1 = s - m[k10%3]
        ms = max(ms,s1)
        s0,k0 = q[0]
        m[k0%3] = min(m[k0%3],s0)
        
    q.pop(0)
    q.append([s,k10])
    
if ms != -10**20:
    print(ms)
else:
    print('NO')

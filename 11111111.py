f = open('input.txt', 'r', encoding = 'utf-8')
out = open('output.txt', 'w')
mx = 0
sch = dict()  #[ n:[b,b],n:[b,b,b], n:[b,b,b,b,b]   ]
for s in f:
    x = s.split()
    sch[int(x[2])] = sch.get(int(x[2]), [] )+[ int(x[3]) ]
    mx = max(mx, int(x[3]))
        
p=sorted(sch.items(), key = lambda x: (-x[1].count(mx), x[0]))

mk = max([v.count(mx) for v in sch.values()])

for n, v in p:
    if v.count(mx) == mk:
        print(str(n)+' ',end='', file=out) # out.write(str(n)+' ')
    
f.close()
out.close()

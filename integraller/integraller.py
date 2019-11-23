f=[]
f.append (2)
f[0] = 2
f[1] = 7
f[3] = 4
for i in range (0,2):
    m = f[i+1] - f[i]
    b = m*(i+1) - f[i+1]
    print(b)
    print(m)




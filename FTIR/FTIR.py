import cv2
import matplotlib.pyplot as plt
import numpy as np
import math 
from scipy.integrate import quad




#T = 1
#n = 40


##img = cv2.imread('C:\\Users\sbese\Desktop\Captures\test1.jpg',-1)#kok -1 1J
#img = cv2.imread('C:\\Users\sbese\Pictures\c\sp1.jpg',-1)
#if img is None:
#    print("Can't load image, please check the path")
    
#pxcounter = []
#pxcounter2 = []
#cn = []
#c0 = []
#f = []


#x = 812
#y = 1136
#x2  = x
#y2 = y

#pxcounter = []
#for i in range(0,x2):
#    pxcounter.append([])
#    for j in range(y2):
#            pxcounter[i].append(i*j)

#for i in range(0,x):
#    pxcounter2.append([i])

#for i in range (0,T):
#    cn.append([i])

#for i in range (0,T):
#    c0.append([i])

#for i in range (0,n):
#    f.append([i])







#for i in range (250,570,20):
#    for j in range (0,x):
        
    
#        px1,px2,px3 = img[i,j]
#        pxcounter[i][j] = px1+px2+px3
#        pxcounter2[i] = (pxcounter[i][j] + pxcounter2[j])
      

#k = 0
#k2 = 0

#for i in range (0,n):
#    k = -2*3.14*1J*i*m.exp(-2*3.14*i) + k

#for z in range (1,T):
#    cn[z] = (1/z) * (pxcounter2[z]*k*m.exp(z)*m.exp(1/z))

#for i in range (0,n):
#    k2 = m.exp(-2*3.14*i) + k2

#for i in range (1,T):
#    c0[i] = (1/i)*(pxcounter2[i])

#for i in range (0,10000):
#    f[i] = k*k2*m.exp(1/T) + c0[i]


#y in range (0,500)
#plt.plot(f,y)
#plt.show()




T = 1
x = np.linspace(-5,5,1000)
armonics = 4

img = cv2.imread('c:\\users\sbese\pictures\c\e.jpg',-1)
if img is None:
    print("can't load image, please check the path")
    

pxcounter2 = []
pxcounter3 = []
cn = []
c0 = []
f = []


w = 311
l = 100


pxcounter = []
for i in range(w):
    pxcounter.append([])
    for j in range(l):
            pxcounter[i].append(i*j)

for i in range(0,l):
    pxcounter2.append([i])

for i in range(0,l):
    pxcounter3.append([i])

cunter = 0
for i in range (0,w):   
    
    for j in range (0,l):
       
        px1,px2,px3 = img[i,j]
        pxcounter[i][j] = px1+px2+px3
        pxcounter3[j] = (pxcounter[i][j] + pxcounter3[j])/2
    
pxcounter2 = pxcounter3

#pxcounter area equals integral of f(x)
#sum2 = 0
#for j in range (1,l):
#    sum2 = sum2 + pxcounter3[j-1] + pxcounter3[j]
#print(sum2)
#sum = int(sum2[0])
#print(sum)
#print(a)
#def an(n,x,sum):
#    a = ((2*sum)/(2*m.pi*n))*np.sin((2*m.pi*n*x)/T)
#    return an

#def a0(n,sum):
#    c = sum
#    return c
#def bn(n,x,sum):
#    b = (-1*((2*sum)/(2*m.pi*n))*np.cos((2*m.pi*n*x)/T))-(2*sum)/(2*m.pi*n)
#    return bn


partialSums = []
for i in range(0,armonics):
    partialSums.append([i])

an = []
for i in range(0,l):
    an.append([i])

bn = []
for i in range(0,l):
    bn.append([i])

a0 = []
for i in range(0,l):
    a0.append([i])

ayedek = []
for i in range(0,l):
    ayedek.append([i])

m = []
for i in range(0,l):
    m.append([i])

b = []
for i in range(0,l):
    b.append([i])


for i in range (0,99):
    
    m[i] = pxcounter2[i+1] - pxcounter2[i]
    b[i] = (m[i]*(i+1) - pxcounter2[i+1])*(-1)
  
    




def fourierSeries(n,x,m,b):  
    
    
  

    


    partialSums = 0
    T = 1
    def integrand(x, m1, b1):
        return m1*x + b1
    def integrand2(x, m1, b1):
        return ((m1*x + b1)*math.cos((2*math.pi*n*x)/T))
    def integrand3(x, m1, b1):
        return ((m1*x + b1)*math.sin((2*math.pi*n*x)/T))

    ecem  = 0    
    for i in range (0,99):
      
        m1 = int(m[i])
        b1 = int(b[i])
        
        #print(m1)
        #print(b1)
        ayedek = (quad(integrand,0,i,args=(m1,b1)))
        
        a0[i] = (1/T)*ayedek[0]
        #print(a0[i])
       

    for i in range (0,99):
        ayedek = (quad(integrand2,0,i,args=(m1,b1)))
        an[i] = (2/T)*ayedek[0]
        #print(an[i])
        

    for i in range (0,99):
        ayedek = (quad(integrand3,0,i,args=(m1,b1)))
        bn[i] = (2/T)*ayedek[0]
        #print(bn[i])






   
    for i in range (0,99):
        partialSums = partialSums + a0[i] + an[i]*math.cos((2*math.pi*n*x)/T) + bn[i]*math.sin((2*math.pi*n*x)/T)   
    return partialSums



        #try:   
   
        #print(partialSums)
        #except: 
            #print("pass")
           # pass
    #print(partialSums)
  
 


f =[]
for j in range (1,armonics):
    for i in x:  
        f.append(fourierSeries(j,i,m,b))
    plt.plot(x,f,color="blue")
    f = []
plt.legend()
plt.show()
    
   


    
    








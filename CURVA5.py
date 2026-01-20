# -*- coding: utf-8 -*-
"""
Created on Wed May 21 09:22:15 2025

@author: Eulogio
"""
import numpy as np
#from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
# READ THE DATA
sst = np.genfromtxt('curva5.dat', delimiter=' ')
fichero = open('curva5m.dat','w')
#print (sst)
xx=sst[:,0]
yy=sst[:,1]
ne=np.size(xx)
print ('first point experimental data')
print (xx[0],yy[0])
xp1 = xx[0]
yp1 = yy[0]
# experimental data relative to first point (0,0)
xx = xx - xp1
yy = yy - yp1
print('number of experimental data:', ne)
print (xx[0],yy[0])
print (xx[ne-1],yy[ne-1])
#print (xx)
#print (yy)
plt.xlim(-200, 300)
plt.ylim(-200, 300)
#sign parameter for reflexion
sss = -1
# w parameter defines the curve
a=35
# rl scale parameter
rl=520
# rotation angle (degree)
arot=-127
# number of points discretization of model 
n=100
# number of points extension of model
nn=100 
# the interval used is [nn1,nn2] between 1 and nn
nn1=32
nn2=83
a=(a*np.pi)/180.0
arot=(arot*np.pi)/180.0
ds=rl/n
xpos=np.zeros([nn]); ypos=np.zeros([nn])
nnn=np.size(xpos)
print('size of xpos:', nnn)
print (xpos[0],ypos[0])
print (xpos[nnn-1],ypos[nnn-1])
x=0.0; y=0.0
xpos[nn1-1]=x; ypos[nn1-1]=y
for i in np.arange(nn1,nn2+1,1):
    s=(i)*ds
    theta=a*np.sin(2.0*np.pi*s/rl)
    x=x+ds*np.cos(theta)
    y=y+ds*np.sin(theta)   
    xpos[i]=x
    ypos[i]=y
for i in np.arange(nn1-1,nn2+1,1):
    x=xpos[i]
    y=ypos[i]
    xpos[i]=x*np.cos(arot)+y*np.sin(arot)
    ypos[i]=-x*np.sin(arot)+y*np.cos(arot)
xpos = xpos * sss 
print (xpos[nn1],ypos[nn1])   
print (xpos[nn2+1],ypos[nn2+1]) 
D1=0.0   
for i in np.arange(nn1-1,nn2+1,1):
  #print (i)  
  di=10e15
  for j in np.arange(0,ne,1):
      #print (j)  
      hx=xpos[i]-xx[j]
      hy=ypos[i]-yy[j]
      h=np.sqrt(hx*hx+hy*hy)
      if h < di:
          di = h
  if di > D1:
      D1 = di        
print('goodness of fit D1:', D1) 
D2=0.0   
for i in np.arange(0,ne,1):
  #print (i)  
  di=10e15
  for j in np.arange(nn1-1,nn2+1,1):
      #print (j)  
      hx=xpos[j]-xx[i]
      hy=ypos[j]-yy[i]
      h=np.sqrt(hx*hx+hy*hy)
      if h < di:
          di = h
  if di > D2:
      D2 = di        
print('goodness of fit D2:', D2)     
print('goodness of fit D1+D2:', D1+D2)          
plt.scatter(xx, yy, s=6, marker='o',c='r')
plt.scatter(xpos[nn1-1:nn2+1],ypos[nn1-1:nn2+1], s=1, marker='o',c='g')
plt.xlabel('Easting (cm)')
plt.ylabel('Northing (cm)')
plt.gca().set_aspect('equal')
plt.show
for i in np.arange(nn1-1,nn2+1,1):
    print(xpos[i]+xp1,ypos[i]+yp1, sep=' ', file=fichero) 
fichero.close()    
#print (xx[0],yy[0])
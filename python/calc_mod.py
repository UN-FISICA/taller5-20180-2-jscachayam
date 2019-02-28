from scipy.misc import imread
import scipy.ndimage as nd
import pylab as p
import numpy as np

def cal(image, hz, dx):
    a=imread(image)
    c=np.array(((a[:,:,0]/3) + (a[:,:,1]/3) + (a[:,:,2]/3)),dtype="int")
    if np.average(c)<255/2:
        b=p.where(c<40,0,255)
    else:
            bf=p.where(c<200,0,255)
            b= np.ones(c.shape,dtype="int")*255 - np.array(bf)
      
    lb,n=nd.label(b)
    y1=[]
    x1=[]
    dt=1/hz
    t=0
    for i in range(n):
        if i<n-1:
            y1.append((nd.measurements.center_of_mass(b,lb,i+2)[0])*dx)    
            t= t + dt
            x1.append(t)
    y=np.array(y1)
    x=np.array(x1)
    f=[]
    f.append(lambda x:np.ones_like(x))
    f.append(lambda x:x)
    f.append(lambda x:x**2)
    Xt=[]
    for fu in f:
        Xt.append(fu(x))
    Xt= np.array(Xt)
    X=Xt.transpose()
    a=np.dot(np.dot(inv(np.dot(Xt,X)),Xt),y)
    print(a[2]*2)

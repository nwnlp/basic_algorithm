import copy
import numpy as np
from matplotlib import pyplot as pl
from matplotlib import animation as ani
records = []
test_data = []
x1 = []
x2 = []
xllim = 0
xrlim = 0
yllim = 0
yrlim = 0
def getTestData():
    global test_data
    x1 = [3,3]
    x2 = [4,3]
    x3 = [1,1]
    x4 = [2,2]
    x5 = [1,2]
    x6 = [1,0]
    x7 = [4,0]
    x8 = [2,3]
    x9 =[2,2.5]
    test_data.append([x1, 1])
    test_data.append([x2, 1])
    test_data.append([x8, 1])
    test_data.append([x9, 1])
    test_data.append([x3, -1])
    test_data.append([x4, -1])
    test_data.append([x5, -1])
    test_data.append([x6, -1])
    test_data.append([x7, -1])
    return test_data
    
def calcGram(test_data):
    gram = np.zeros((len(test_data), len(test_data)), dtype=np.int)
    index_x = 0
    for d1 in test_data:
        x1 = d1[0]
        index_y = 0
        for d2 in test_data:
            x2 = d2[0]
            gram[index_x][index_y] = np.inner(x1, x2)
            index_y+=1
        index_x+=1
    return gram

def addjust_dual(test_data, gram, a, b):
    splited = 0
    for i in range(0,len(test_data)):
        yi = test_data[i][1]
        wxi = 0
        for j in range(0, len(test_data)):
            aj = a[j]
            yj = test_data[j][1]
            xjxi = gram[i][j]
            wxi+=aj*yj*xjxi
        if(yi*(wxi+b[0]) <=0):
            a[i]+=1
            b[0]+=yi
            record = []
            record.append(getWeight(a))
            record.append(b[0])
            records.append(record)
            splited = 0
        else:
            splited+=1
        
    if(splited >= len(test_data)):
        return 0
    else:
        return -1

def getWeight(a):
    #print(a)
    w = [0, 0]
    for i in range(0, len(test_data)):
        xi = np.array(test_data[i][0])
        yi = test_data[i][1]
        ai = a[i]
        w = w+ai*yi*xi
    #print(w)
    return w
def perceptron_dual(test_data):
    a = [0]*len(test_data)
    b = [0]
    print(test_data)
    gram = calcGram(test_data)
   
    while 1:
        if(addjust_dual(test_data, gram, a, b) == -1):
            continue
        else:
            break
    print(getWeight(a))
    print(b[0])
        
def addjust_org(test_data, w, b):
    splited = 0
    step = 0.5
    for data in test_data:
        xi = data[0]
        yi = data[1]
        if yi*(np.inner(xi, w)+b[0]) <= 0:
            w[0] = w[0]+yi*xi[0]*step
            w[1] = w[1]+yi*xi[1]*step
            b[0] = b[0]+yi*step
            record = []
            record.append(copy.copy(w))
            record.append(b[0])
            records.append(record)
            splited = 0
        else:
            splited += 1
            
    if(splited >= len(test_data)):
        return 0
    else:
        return -1
        
def perceptron_org(test_data):
    b = [0]
    w = [0, 0]
    while 1:
        if(addjust_org(test_data, w, b) == -1):
            continue
        else:
            break
    print(w)
    print(b[0])            
def animate(i):
    global records,ax,line,lastline,xllim,xrlim,yllim,yrlim
    x1 = xllim
    x2 = xrlim
    y1 = yllim
    y2 = yrlim 
    w = records[i][0]
    #print(w)
    w0 = w[0]
    w1 = w[1]
    b = records[i][1]
    if w0 == 0 and w1 == 0:
        return lastline,
    if w1 == 0:
        x1 = -(b/w0)
        x2 = x1  
    else:    
        y1 = -(b+w0*x1)/w1
        y2 = -(b+w0*x2)/w1
    line.set_data([x1,x2],[y1,y2])
    lastline, = line,
    return line,

def init():

    line.set_data([],[])
    for data in test_data:
        if data[1] == 1:
            pl.plot(data[0][0],data[0][1],'or')    
        else:
            pl.plot(data[0][0],data[0][1],'ob')
    return line,

if __name__ == "__main__":
    getTestData()
    #perceptron_dual(test_data)
    perceptron_org(test_data)
    print('learning steps:%d' %(len(records)))
    for data in test_data:
        x1.append(data[0][0])
        x2.append(data[0][1])
fig = pl.figure()
xllim = min(x1)-3
xrlim = max(x1)+3
yllim = min(x2)-3
yrlim = max(x2)+3        
ax = pl.axes(xlim=(xllim, xrlim), ylim= (yllim,yrlim) )            
line,=ax.plot([],[],'g',lw=1)
lastline, = line,
animat=ani.FuncAnimation(fig,animate,init_func=init,frames=len(records),interval=100,repeat=False,blit=True)
pl.show()

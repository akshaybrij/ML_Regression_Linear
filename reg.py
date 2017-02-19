import numpy as np
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import style
point=genfromtxt('D:/data.csv',delimiter=',')


def low_error(m,b,point):
    total_err=0
    for i in range(0,len(point)):
        x=point[i,0]
        y=point[i,1]
        total_err+=(y - (m * x + b))**2

    return total_err/float(len(point))
def step_gradient(m_c,b_c,lra,point):
    m_grad=0
    b_grad=0
    N=float(len(point))
    for i in range(0,len(point)):
        x=point[i,0]
        y=point[i,1]
        m_grad+=-(2  ) * (y - ( m_c * x) + b_c)

        b_grad+=-(2 / N) * x * (y - (m_c * x) + b_c)

    new_b = b_c - (lra * b_grad)
    new_m = m_c - (lra * m_grad)
    #plt.scatter(new_m,new_b)
    #plt.show()

    return [new_m,new_b]


def gradient_run(m_rad,b_rad,lr,iter,point):
    for i in range(iter):
        m,b = step_gradient(m_rad,b_rad,lr,np.array(point))
    return [m,b]

def run():
    initial_m=0;
    initial_b=0;
    learn_rate=0.0001
    iteration=1000
    print 'starting {0},{1},{2}'.format(initial_m,initial_b,low_error(initial_m,initial_b,point))
    [m,b]=gradient_run(initial_m,initial_b,learn_rate,iteration,point)
    print m,b
    print 'end {0},{1},{2}'.format(m,b,low_error(m,b,point))
    ls=[]
    ds=[]
    for i in range(len(point)):
        x=point[i,0]
        ls.append(x)
        z = m * x + b
        ds.append(z)
        y=point[i,1]
        plt.scatter(x,y)
    print m,b
    plt.plot(ls,ds)
    plt.show()




if __name__=='__main__':
    run()

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

myX = np.loadtxt('GaCo03_01.txt', usecols=range(1, 19))  # 第一列时间不要
# myX = np.load('X_sample.npy')
print(myX.shape)
plt.axis([0, 121, 0, 1305])
plt.plot(myX)


nSample = 1000

def RandSampleTimesteps(X, nSample=1000):
    X_new = np.zeros(X.shape)
    tt = np.zeros((nSample, X.shape[1]), dtype=int)
    for i in range(X.shape[1]):
        tt[1:-1, i] = np.sort(np.random.randint(1, X.shape[0] - 1, nSample - 2))
    # tt[1:-1,0] = np.sort(np.random.randint(1,X.shape[0]-1,nSample-2))
    # tt[1:-1,1] = np.sort(np.random.randint(1,X.shape[0]-1,nSample-2))
    # tt[1:-1,2] = np.sort(np.random.randint(1,X.shape[0]-1,nSample-2))
    tt[-1, :] = X.shape[0] - 1
    return tt


def DA_RandSampling(X, nSample=1000):
    tt = RandSampleTimesteps(X, nSample)
    X_new = np.zeros(X.shape)
    for i in range(X.shape[1]):
        X_new[:, i] = np.interp(np.arange(X.shape[0]), tt[:, i], X[tt[:, i], i])
    # X_new[:,0] = np.interp(np.arange(X.shape[0]), tt[:,0], X[tt[:,0],0])
    # X_new[:,1] = np.interp(np.arange(X.shape[0]), tt[:,1], X[tt[:,1],1])
    # X_new[:,2] = np.interp(np.arange(X.shape[0]), tt[:,2], X[tt[:,2],2])
    return X_new


fig = plt.figure(figsize=(15, 4))
for ii in range(8):
    ax = fig.add_subplot(2, 4, ii + 1)
    ax.plot(DA_RandSampling(myX))
    ax.set_xlim([0, 121])
    ax.set_ylim([0, 1310])
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

myX = np.loadtxt('GaCo03_01.txt', usecols=range(1, 19))  # 第一列时间不要
# myX = np.load('X_sample.npy')
print(myX.shape)
# plt.plot(myX)

nPerm = 4
minSegLength = 100


def DA_Permutation(X, nPerm=4, minSegLength=10):
    X_new = np.zeros(X.shape)
    idx = np.random.permutation(nPerm)
    bWhile = True
    while bWhile == True:
        segs = np.zeros(nPerm + 1, dtype=int)
        segs[1:-1] = np.sort(np.random.randint(minSegLength, X.shape[0] - minSegLength, nPerm - 1))
        segs[-1] = X.shape[0]
        if np.min(segs[1:] - segs[0:-1]) > minSegLength:
            bWhile = False
    pp = 0
    for ii in range(nPerm):
        x_temp = X[segs[idx[ii]]:segs[idx[ii] + 1], :]
        X_new[pp:pp + len(x_temp), :] = x_temp
        pp += len(x_temp)
    return (X_new)


fig = plt.figure(figsize=(15, 4))
for ii in range(8):
    ax = fig.add_subplot(2, 4, ii + 1)
    ax.plot(DA_Permutation(myX))
    ax.set_xlim([0, 121])
    ax.set_ylim([0, 1310])
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

myX = np.loadtxt('GaCo03_01.txt', usecols=range(1, 19))  # 第一列时间不要
print(myX.shape)


sigma = 0.2
knot = 4

def GenerateRandomCurves(X, sigma=0.2, knot=4):
    xx = (np.ones((X.shape[1],1))*(np.arange(0,X.shape[0], (X.shape[0]-1)/(knot+1)))).transpose()
    yy = np.random.normal(loc=1.0, scale=sigma, size=(knot+2, X.shape[1]))
    x_range = np.arange(X.shape[0])
    # 生成曲线数据
    curves = []

    for i in range(X.shape[1]):
        cs = CubicSpline(xx[:, i], yy[:, i])
        curves.append(cs(x_range))

    return np.array(curves).transpose()

def DA_MagWarp(X, sigma):
    return X * GenerateRandomCurves(X, sigma)

# fig, axes = plt.subplots(1, 2, figsize=(15, 4))
#
# # 第一个子图：原始数据
# axes[0].plot(myX)
# axes[0].set_title("An example of 1min acceleration data")
# axes[0].axis([0, 121, 0, 1305])
#
# # 第二个子图：经过缩放处理后的数据
# axes[1].plot(DA_MagWarp(myX, sigma))
# axes[1].set_xlim([0, 121])
# axes[1].set_ylim([0, 1305])
#
# plt.show()

fig = plt.figure(figsize=(15, 4))
for ii in range(8):
    ax = fig.add_subplot(2, 4, ii + 1)
    ax.plot(DA_MagWarp(myX, sigma))
    # ax.set_xlim([0, 121 * 5])  # *5代表五个周期
    ax.set_xlim([0, 121])  # *5代表五个周期
    ax.set_ylim([0, 1310])
plt.show()
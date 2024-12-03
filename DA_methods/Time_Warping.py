import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

myX = np.loadtxt('GaCo03_01.txt', usecols=range(1, 19))  # 第一列时间不要
print(myX.shape)

sigma = 0.2
knot = 4


def GenerateRandomCurves(X, sigma=0.2, knot=4):
    xx = (np.ones((X.shape[1], 1)) * (np.arange(0, X.shape[0], (X.shape[0] - 1) / (knot + 1)))).transpose()
    yy = np.random.normal(loc=1.0, scale=sigma, size=(knot + 2, X.shape[1]))
    x_range = np.arange(X.shape[0])
    # 生成曲线数据
    curves = []

    for i in range(X.shape[1]):
        cs = CubicSpline(xx[:, i], yy[:, i])
        curves.append(cs(x_range))

    return np.array(curves).transpose()


def DistortTimesteps(X, sigma=0.2):
    tt = GenerateRandomCurves(X, sigma)  # Regard these samples aroun 1 as time intervals
    tt_cum = np.cumsum(tt, axis=0)  # Add intervals to make a cumulative graph
    # Make the last value to have X.shape[0]
    # t_scale = [(X.shape[0] - 1) / tt_cum[-1, 0], (X.shape[0] - 1) / tt_cum[-1, 1], (X.shape[0] - 1) / tt_cum[-1, 2]]

    # 确保最后一个值等于 X.shape[0]
    t_scale = (X.shape[0] - 1) / tt_cum[-1]

    for i in range(X.shape[1]):
        tt_cum[:, i] = tt_cum[:, i] * t_scale[i]
    # tt_cum[:, 0] = tt_cum[:, 0] * t_scale[0]
    # tt_cum[:, 1] = tt_cum[:, 1] * t_scale[1]
    # tt_cum[:, 2] = tt_cum[:, 2] * t_scale[2]
    return tt_cum



def DA_TimeWarp(X, sigma=0.2):
    tt_new = DistortTimesteps(X, sigma)
    X_new = np.zeros(X.shape)
    x_range = np.arange(X.shape[0])
    for i in range(X.shape[1]):
        X_new[:, i] = np.interp(x_range, tt_new[:, i], X[:, i])
    # X_new[:,0] = np.interp(x_range, tt_new[:,0], X[:,0])
    # X_new[:,1] = np.interp(x_range, tt_new[:,1], X[:,1])
    # X_new[:,2] = np.interp(x_range, tt_new[:,2], X[:,2])
    return X_new


# fig = plt.figure(figsize=(15, 4))
# for ii in range(8):
#     ax = fig.add_subplot(2, 4, ii + 1)
#     ax.plot(DA_TimeWarp(myX, sigma))
#     ax.set_xlim([0, 121 * 5])  # *5代表五个周期
#     ax.set_ylim([0, 1310])
# plt.show()

fig, axes = plt.subplots(1, 2, figsize=(15, 4))

# 第一个子图：原始数据
axes[0].plot(myX)
axes[0].set_title("An example of 1min acceleration data")
axes[0].axis([0, 121, 0, 1305])

# 第二个子图：经过缩放处理后的数据
axes[1].plot(DA_TimeWarp(myX, sigma))
axes[1].set_xlim([0, 121])
axes[1].set_ylim([0, 1310])

plt.show()
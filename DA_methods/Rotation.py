import numpy as np
import matplotlib.pyplot as plt
from transforms3d.axangles import axangle2mat

myX = np.loadtxt('GaCo03_01.txt', usecols=range(1, 19))  # 第一列时间不要
# myX = np.load('X_sample.npy')
print(myX.shape)
# plt.plot(myX)
# plt.axis([0, 121, 0, 1305])
# plt.show()

def DA_Rotation(X):
    rotated_X = np.zeros_like(X)  # 创建一个与输入数据形状相同的全零数组来保存旋转后的数据
    for i in range(X.shape[1] // 3):  # 将18个特征分成6组，每组包含3个特征
        axis = X[:, i*3:(i+1)*3].mean(axis=0)  # 取每组特征的平均值作为轴向量
        axis /= np.linalg.norm(axis)  # 规范化轴向量为长度为1
        angle = np.random.uniform(low=-np.pi, high=np.pi)  # 生成随机旋转角度
        r = axangle2mat(axis, angle)  # 根据轴和角度生成旋转矩阵
        rotated_X[:, i*3:(i+1)*3] = np.matmul(X[:, i*3:(i+1)*3], r.T)  # 对每组特征应用旋转矩阵
    return rotated_X

# def DA_Rotation(X):
#     axis = np.random.uniform(low=-1, high=1, size=X.shape[1])
#     angle = np.random.uniform(low=-np.pi, high=np.pi)
#     return np.matmul(X, axangle2mat(axis, angle))

#
# fig = plt.figure(figsize=(15, 4))
# for ii in range(8):
#     ax = fig.add_subplot(2, 4, ii + 1)
#     ax.plot(DA_Rotation(myX))
#     ax.set_xlim([0, 121])
#     ax.set_ylim([-1210, 1210])
# plt.show()
fig, axes = plt.subplots(1, 2, figsize=(15, 4))

# 第一个子图：原始数据
axes[0].plot(myX)
axes[0].set_title("An example of 1min acceleration data")
axes[0].axis([0, 121, 0, 1305])

# 第二个子图：经过缩放处理后的数据
axes[1].plot(DA_Rotation(myX))
axes[1].set_xlim([0, 121])
axes[1].set_ylim([0, 1305])

plt.show()
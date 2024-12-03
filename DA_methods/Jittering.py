import numpy as np
import matplotlib.pyplot as plt

myX = np.loadtxt('GaCo03_01.txt', usecols=range(1, 19))  # 第一列时间不要
print(myX.shape)
print(myX)

# plt.plot(myX)
# plt.title("An example of GaCo03_01 acceleration data (18 features)")
# plt.axis([0, 121, 0, 1305])

# # 获取图中的所有线条对象
# lines = plt.gca().get_lines()
#
# # 打印线条数量
# print("图中的线条数量：", len(lines))
# plt.show()

sigma = 2

def DA_Jitter(X, sigma=0.05):
    myNoise = np.random.normal(loc=0, scale=sigma, size=X.shape)
    return X + myNoise

myX_processed = DA_Jitter(myX,sigma)
# print(myX_processed.shape)
# print(myX_processed)

fig, axes = plt.subplots(1, 2, figsize=(15, 4))

# 第一个子图：原始数据
axes[0].plot(myX)
axes[0].set_title("An example of 1min acceleration data")
axes[0].axis([0, 121, 0, 1305])

# 第二个子图：经过缩放处理后的数据
axes[1].plot(DA_Jitter(myX, sigma))
axes[1].set_xlim([0, 121])
axes[1].set_ylim([0, 1305])

plt.show()
# fig = plt.figure(figsize=(15, 4))
# for ii in range(8):
#     ax = fig.add_subplot(2, 4, ii + 1)
#     ax.plot(DA_Jitter(myX, sigma))
#     ax.set_xlim([0, 121 ])  # *5代表五个周期
#     ax.set_ylim([0, 1310])
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

myX = np.loadtxt('GaCo03_01.txt', usecols=range(1, 19))  # 第一列时间不要
print(myX.shape)

sigma = 0.1

def DA_Scaling(X, sigma=0.1):
    scalingFactor = np.random.normal(loc=1.0, scale=sigma, size=(1,X.shape[1])) # shape=(1,3)
    myNoise = np.matmul(np.ones((X.shape[0],1)), scalingFactor)
    return X*myNoise


fig, axes = plt.subplots(1, 2, figsize=(15, 4))

# 第一个子图：原始数据
axes[0].plot(myX)
axes[0].set_title("An example of 1min acceleration data")
axes[0].axis([0, 121, 0, 1305])

# 第二个子图：经过缩放处理后的数据
axes[1].plot(DA_Scaling(myX, sigma))
axes[1].set_xlim([0, 121])
axes[1].set_ylim([0, 1305])

plt.show()
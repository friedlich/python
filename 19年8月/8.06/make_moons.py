import sklearn
import sklearn.datasets

sklearn.datasets.make_circles(n_samples=100, shuffle=True, noise=None, random_state=None, factor=0.8)
# 生成环形数据
# factor ：外圈与内圈的尺度因子<1
sklearn.datasets.make_moons(n_samples=100, shuffle=True, noise=None, random_state=None)
# 生成半环形图
from sklearn.datasets import make_circles
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import numpy as np
 
fig=plt.figure(1)
x1,y1=make_circles(n_samples=1000,factor=0.5,noise=0.1)
print(x1.shape)
print(y1.shape)
plt.subplot(121)
plt.title('make_circles function example')
plt.scatter(x1[:,0],x1[:,1],marker='o',c=y1)
 
plt.subplot(122)
x1,y1=make_moons(n_samples=1000,noise=0.1)
print(x1.shape)
print(y1.shape)
plt.title('make_moons function example')
plt.scatter(x1[:,0],x1[:,1],marker='o',c=y1)
plt.show()

# 下面有两种方法都可以：
import numpy as np
a=np.asarray([[10,20],[101,201]])
print(a)
print(a.shape)
# print(a.reshape(1,-1).T)

print()
print()

# a=a[:,:,np.newaxis]
# print(a.shape)
# b= a.repeat([3],axis=2)
# print(b.shape,b)

image = np.expand_dims(a, axis=2)
# np.expand_dims:用于扩展数组的形状
# np.expand_dims(a, axis=0)表示在0位置添加数据
print(image)
print(image.shape)
print()
image = np.concatenate((image, image, image), axis=-1) # -1是最后一层叠加的意思

print(image)
print(image.shape)
# print(image.reshape(1,-1).T)

print(np.concatenate((image, image, image), axis=1)) # 这里的1的话应该是指非0层都叠加了
print(np.concatenate((image, image, image), axis=1).shape)

print(np.concatenate((image, image, image), axis=0))
print(np.concatenate((image, image, image), axis=0).shape) # 这里的0的话应该是指非1层都叠加了

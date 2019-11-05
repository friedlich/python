# -*- coding: utf8 -*-
import sys
import cv2
import openpyxl
# 读取头像和国旗图案
print(sys.path[0])
print(sys.path[0]+'\\head.jpg')
img_head = cv2.imread(sys.path[0]+'\\head.jpg')
print(type(img_head))
img_flag = cv2.imread(sys.path[0]+'\\flag.jpg')
# 获取头像和国旗图案宽度
w_head, h_head = img_head.shape[:2]
w_flag, h_flag = img_flag.shape[:2]
# 计算图案缩放比例
scale = w_head / w_flag / 4
# 缩放图案
img_flag = cv2.resize(img_flag, (0, 0), fx=scale, fy=scale)
# 获取缩放后新宽度
w_flag, h_flag = img_flag.shape[:2]
# 按3个通道合并图片
for c in range(0, 3):
    img_head[w_head - w_flag:, h_head - h_flag:, c] = img_flag[:, :, c]
# 保存最终结果
cv2.imwrite(sys.path[0]+'\\new_head.jpg', img_head)
import cv2
import os

"""
cv2.WINDOW_NORMAL    # 用户可以改变这个窗口大小
cv2.WINDOW_AUTOSIZE    # 窗口大小自动适应图片大小，并且不可手动更改。
cv2.WINDOW_FREERATIO    # 自适应比例
cv2.WINDOW_KEEPRATIO    # 保持比例
cv2.WINDOW_OPENGL    # 窗口创建的时候会支持OpenGL
"""

path = "D:\\turtle.1"
filenames = os.listdir(path)  # 列出文件
print(filenames)
for i in range(5):  # 逐个打开文件
    filepath = os.path.join(path, filenames[i])
    print(filepath)

    img = cv2.imread(filepath)
    cv2.namedWindow("img_name", cv2.WINDOW_NORMAL)  # 使用cv2.WINDOW_NORMAL创造"img_name"
    cv2.resizeWindow("img_name", 700, int(990))  # 界定窗口范围
    cv2.imshow("img_name", img)  # 在窗口内打开图片
    # cv2.waitKey(3000)  # waitkey控制着imshow的持续时间
    if i == 0 or i == 1 or i == 2 or i == 3:
        cv2.waitKey(2000)
    else:
        cv2.waitKey()

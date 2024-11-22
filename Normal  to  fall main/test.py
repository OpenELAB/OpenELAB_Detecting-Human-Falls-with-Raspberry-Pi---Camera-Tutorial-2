import cv2
import numpy as np

# 打开默认摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        print("无法读取摄像头数据")
        break

    # 显示捕获的帧
    cv2.imshow('capture', frame)

    # 按下 'q' 键时保存图像并退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('takephoto2.jpg', frame)
        print('Photo taken successfully!')
        break

# 释放摄像头资源并关闭窗口
cap.release()
cv2.destroyAllWindows()

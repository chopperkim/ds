# openCV 컴퓨터 비전 및 머신러닝 라이브러리 얼굴인식, 객체 식별, 이미지 결합 및 전처리
import cv2
import matplotlib.pyplot as plt
# 이미지 회색으로
image = cv2.imread('images/plane.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(image, cmap='gray')
plt.show()
# 이미지 작게
image = cv2.imread('images/plane.jpg', cv2.COLOR_BGR2RGB)
img_50 = cv2.resize(image, (50, 50))
plt.imshow(img_50)
plt.show()
# 이미지 흐리게
image_blur = cv2.blur(image, (100,100))
plt.imshow(image_blur)
plt.show()
import numpy as np
kernel = np.array([[0, -1, 0]
                  ,[-1, 5, -1]
                  ,[0, -1, 0]])
conv = cv2.filter2D(image_blur, -1, kernel)
plt.imshow(conv)
plt.show()

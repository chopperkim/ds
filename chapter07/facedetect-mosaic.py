import sys, cv2, re

# 입력 파일 지정하기
image_file = input("이미지 파일 경로와 이름을 입력하세요.")
if len(image_file) == 0:
    print("no input file")
    quit()

print(image_file)
# 출력 파일 이름
output_file = re.sub(r'\.jpg|jpeg|PNG$', '-mosaic.jpg', image_file)
mosaic_rate = 30

# 캐스캐이드 파일 경로 지정하기
cascade_file = "haarcascade_frontalface_alt.xml"

# 이미지 읽어 들이기
image = cv2.imread(image_file)
print(image)
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 인식 실행하기
cascade = cv2.CascadeClassifier(cascade_file)

face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

if len(face_list) == 0:
    print("no face")
    quit()

print(face_list)
color = (0, 0, 255)
for x, y, w, h in face_list:
    face_img = image[y:y + h, x:x + w]
    face_img = cv2.resize(face_img, (w//mosaic_rate, h//mosaic_rate))
    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
    # 원래 이미지에 붙이기
    image[y:y+h, x:x+w] = face_img

# 렌더링 결과를 파일에 출력
cv2.imwrite(output_file, image)

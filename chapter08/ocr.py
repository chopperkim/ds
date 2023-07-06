import cv2
import pytesseract


def recognize_license_plate(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 이미지 전처리
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    # 가장자리 감지
    edges = cv2.Canny(gray, 50, 150)

    # 가장자리에서 컨투어 찾기
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 번호판 영역 찾기
    license_plate = None
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if 2.5 < aspect_ratio < 4.5:  # 번호판의 폭과 높이 비율을 기준으로 선택
            license_plate = gray[y:y + h, x:x + w]
            break

    if license_plate is not None:
        # Tesseract OCR을 사용하여 번호판 인식
        license_plate_text = pytesseract.image_to_string(license_plate, config='--psm 7')
        return license_plate_text
    else:
        return "번호판을 찾을 수 없습니다."


# 이미지 경로 설정
image_path = 'images/1.jpg'

# 번호판 인식 호출
result = recognize_license_plate(image_path)

# 결과 출력
print("인식 결과:", result)
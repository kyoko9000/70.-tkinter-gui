import cv2

cap = cv2.VideoCapture(0)
dectector = cv2.QRCodeDetector()

while True:
    _, frame = cap.read()
    data, _, _ = dectector.detectAndDecode(frame)
    if data:
        a = data
        print(a)
        break

    cv2.imshow("QR-code", frame)
    if cv2.waitKey(1) == ord('q'):
        break

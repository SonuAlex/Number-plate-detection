import cv2
import time
cpt = 0
maxFrames = 100

count = 0
cap = cv2.VideoCapture("D:/GitHub Clones/Number-plate-detection/carVideo/mycarplate.mp4")
while cpt < maxFrames:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame = cv2.resize(frame, (1080, 500))
    cv2.imshow('frame', frame)
    cv2.imwrite('D:/GitHub Clones/Number-plate-detection/images/numberplate_' + str(cpt) + '.jpg', frame)
    time.sleep(0.1)
    cpt += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
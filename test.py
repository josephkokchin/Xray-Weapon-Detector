import cv2
vid = cv2.VideoCapture('/home/yinghuit/Documents/Git/XrayUI/public/video.mp4')
while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break
vid.release()
cv2.destroyAllWindows()
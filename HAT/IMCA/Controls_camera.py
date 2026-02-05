from picamera2 import Picamera2
import cv2
import time


picam2 = Picamera2()
picam2.start()

time.sleep(3)

frame = picam2.capture_array()

cv2.imshow("Test Image", frame)
cv2.waitKey(0)

picam2.stop()
cv2.destroyAllWindows()
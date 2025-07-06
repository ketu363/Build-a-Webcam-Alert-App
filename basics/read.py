# Open CV library its a python library use to do image processing like capture image from webcam.
# Open cv uses bgr (blue green red ) other libraries may use bgr(blue, green red)
import cv2

array = cv2.imread("image.png")

print(array.shape)
# Array shape will return (3, 4, 3) means 3 columns, 4 rows, 3 color channels

print(array)

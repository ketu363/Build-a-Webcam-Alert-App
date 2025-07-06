import cv2
import time

# To start the vidio from ur camera
# If you have laptop then put 0 to use it as main camera and if you attached secondary camera put 1 to use that as main camera
video = cv2.VideoCapture(0)
time.sleep(1)

# We are creating a first frame variable that we use to capture the 1st frame and that will be used to compare with all different frame
first_frame = None

while True:
    check, frame = video.read()
    # Make the color image in gray image so it will reduce the data
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # To make calculation more efficient we will apply gaussian blur method
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)


    # Storing 1st frame
    if first_frame is None:
        first_frame =  gray_frame_gau

    # Make differences between 1st frame and the other fame to get any change to detect the object.
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)


    # Classifying the delta pixels because the quality of image is very noisy and not able to discriminate the new object so we make the ney object brigt and rest black
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    # To remove the noise we delay it
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # imshow show your vidio
    cv2.imshow("My video", thresh_frame)

    # To found counters (detect counters around the white area of the object)
    contours, check =cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if there are two objects and more in the frame detect then it wii calculate the area and if it's occupied area is very small it will reject that as an object.
    for contour in contours:
        # it will pass if the object area less than 1ok pixl.
        if cv2.contourArea(contour) < 5000:
            continue
        # otherwise if object area pixl is grater than 10k pixl it will find the  x,y corner( point on the object) and from x,y it will find width and height of the object
        x, y, w, h =cv2.boundingRect(contour)
        # This will create the rectangle around the original fram (frame1).
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Will show the color vidio with gree rectangle
    cv2.imshow("Vidio", frame)
   # it's create keyboard key object and if user press q it will stop the program
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()

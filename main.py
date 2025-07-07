import os
import cv2
import time
import glob
from  emailing import send_email
from threading import Thread

# To start the vidio from ur camera
# If you have laptop then put 0 to use it as main camera and if you attached secondary camera put 1 to use that as main camera
video = cv2.VideoCapture(0)
time.sleep(1)

# We are creating a first frame variable that we use to capture the 1st frame and that will be used to compare with all different frame
first_frame = None
status_list = []

# to store the images per frame making counter
count = 1

# clean the image folder after sending mail
def clean_folder():
    print("clean_folder function started")
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
    print("clean_folder function ended")

while True:
    status = 0
    check, frame = video.read()

    # This ensures image_with_object always exists — either as None or as a valid image path (when an object is detected and image is saved).
    image_with_object = None

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
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        if rectangle.any():
            status = 1
            # To Store image
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            # find the best image to send in the email
            all_images = glob.glob("images/*.png")
            # return the image that is in middle
            index = int(len(all_images) / 2)
            # return the one image with the middle of all images like is 18 image it return 18/2 9th image index item
            image_with_object = all_images[index]


    status_list.append(status)
    # get the last two digit of the list
    status_list = status_list[-2:]

    # if last two item of list , 1st item ==1 and 2nd item ==0 means object went from the frame
    if status_list[0] == 1 and status_list[1] == 0 and image_with_object:
        # will send email if any object will detect

        # Creating threading for the sending mail this will allow the function to run in the background
        email_thread = Thread(target=send_email, args=(image_with_object,))
        email_thread.daemon = True

        # starting the thread
        email_thread.start()


    print(status_list)

    # Will show the color vidio with gree rectangle
    cv2.imshow("Vidio", frame)
    # it's create keyboard key object and if user press q it will stop the program
    key = cv2.waitKey(1)

    if key == ord("q"):
        # creating thread for cleaning the folder
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True
        clean_thread.start()

        break


video.release()

# if email_thread is not None:
#     email_thread.join()
#
# print("Program safely ended after email was sent.")


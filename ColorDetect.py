# Python code for Multiple Color Detection

import cap as cap

import numpy as np

import cv2



# Capturing video through webcam

webcam = cv2.VideoCapture(0)



# Start a while loop

while (1):



    # Reading the video from the

    # webcam in image frames

    _, imageFrame = webcam.read()



    # Convert the imageFrame in

    # BGR(RGB color space) to

    # HSV(hue-saturation-value)

    # color space

    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)



    # Set range for red color and

    # define mask

    red_lower = np.array([136, 87, 111], np.uint8)

    red_upper = np.array([180, 255, 255], np.uint8)

    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    green_lower = np.array([25, 52, 72], np.uint8)

    green_upper = np.array([102, 255, 255], np.uint8)

    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    blue_lower = np.array([94, 80, 2], np.uint8)

    blue_upper = np.array([120, 255, 255], np.uint8)

    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    kernel = np.ones((5, 5), "uint8")

    red_mask = cv2.dilate(red_mask, kernel)

    res_red = cv2.bitwise_and(imageFrame, imageFrame,

                              mask=red_mask)



    green_mask = cv2.dilate(green_mask, kernel)

    res_green = cv2.bitwise_and(imageFrame, imageFrame,

                                mask=green_mask)



    blue_mask = cv2.dilate(blue_mask, kernel)

    res_blue = cv2.bitwise_and(imageFrame, imageFrame,

                               mask=blue_mask)

    contours, hierarchy = cv2.findContours(green_mask,

                                           cv2.RETR_TREE,

                                           cv2.CHAIN_APPROX_SIMPLE)



                                               

    x2 = 0

    y2 = 0



    

    for pic, contour in enumerate(contours):

        cv2.line(imageFrame,(320,0),(320,480),(0,200,0,50),5)

        cv2.line(imageFrame,(0,240),(640,240),(0,200,0,50),5)

        area = cv2.contourArea(contour)

        if (area > 350):

            x, y, w, h = cv2.boundingRect(contour)

            x2 = (x + w)/2

            y2 = (y + h)/2

            imageFrame = cv2.rectangle(imageFrame, (x, y),

                                       (x+w, y+h),

                                       (0, 255, 0), 2)

                    

            cv2.putText(imageFrame, "", (x ,y),

                        cv2.FONT_HERSHEY_SIMPLEX,

                        1.0, (0, 255, 0))



    # Program Termination

    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)

    if cv2.waitKey(10) & 0xFF == ord('q'):

        cap.release()

        cv2.destroyAllWindows()

        break


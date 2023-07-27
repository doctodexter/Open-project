import RPi.GPIO as GPIO
import time
import cap as cap
import numpy as np
import cv2
import dlib
import math
webcam = cv2.VideoCapture(0)
GPIO.setmode(GPIO.BCM)
servo_pin = 17
servo_pin1 = 18
pwm_freq = 50
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(servo_pin1, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, pwm_freq)
servo_pwm1 = GPIO.PWM(servo_pin1,pwm_freq)
servo_pwm1.start(7.5)
servo_pwm.start(7.5)
def move_servo(angle):
    duty_cycle = 2.5 + angle / 18.0
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5) 
def move_servo1(angle):
    duty_cycle = 2.5 + angle / 18.0
    servo_pwm1.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  
while (1):
    _, imageFrame = webcam.read()
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
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
            servoangle = 90
            servoangle1 = 90
            if(x2 > 160):
				servoangle += 5
				move_servo(servoangle)
			else:
				servoangle += 5
				move_servo(servoangle) 
            dist = math.dist((x2,y2),(160,120))
            if(dist < 25):
                print("poza")
            else:
                print("nu poza")
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x+w, y+h),
                                       (0, 255, 0), 2)
                    
            cv2.putText(imageFrame, "Roata", (x ,y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))

    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

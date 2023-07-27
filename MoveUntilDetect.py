import RPi.GPIO as GPIO
import time
import cv2
import dlib
GPIO.setmode(GPIO.BCM)
servo_pin = 17
servo_pin1 = 18
pwm_freq = 50
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(servo_pin1, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, pwm_freq)
servo_pwm1 = GPIO.PWM(servo_pin1,pwm_freq)
def move_servo(angle):
    duty_cycle = 2.5 + angle / 18.0
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5) 
def move_servo1(angle):
    duty_cycle = 2.5 + angle / 18.0
    servo_pwm1.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)  
servo_pwm1.start(7.5)
try:
    servo_pwm.start(7.5)
    
    while True:
        for angle in range(160, -19, -10):
            move_servo1(angle)
            for angle1 in range(180, -1, -15):
                move_servo(angle1)
        for angle in range(20, 160, 10):
            move_servo1(angle)
            for angle1 in range(1, 180, 15):
                move_servo(angle1)


except KeyboardInterrupt:
    servo_pwm.stop()
    GPIO.cleanup()

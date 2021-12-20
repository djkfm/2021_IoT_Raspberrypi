from typing import final
import RPi.GPIO as GPIO
import time

SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50) # 50Hz, 1Period = 20ms
pwm.start(7.5) # 7.5(0도)

try:
    while True:
        val = input('1:-90, 2:0, 3:+90, 9:Quit> ')
        if val == '1':
            pwm.ChangeDutyCycle(5) #-90도, 20ms * 5% = 1ms
        elif val == '2':
            pwm.ChangeDutyCycle(7.5) #0도, 20ms * 7.5% = 1.5ms
        elif val == '3':
            pwm.ChangeDutyCycle(10) # +90eh, 20ms * 10% = 2ms
        elif val == '9':
            break
finally:
    pwm.stop()
    GPIO.cleanup()
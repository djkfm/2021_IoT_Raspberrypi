import RPi.GPIO as GPIO

SERVO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

#주파수 설정: 50hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5) #0도

try:
    while True:
        val = input('1: 0도, 2: -90도, 3: 90도, 9: Exit>')
        if val == '1':
            pwm.ChangeDutyCycle(7.5)#0도
        elif val == '2':
            pwm.ChangeDutyCycle(5)
        elif val == '3':
            pwm.ChangeDutyCycle(10)
        elif val == '9':
            break
finally:
     pwm.stop()
     GPIO.cleanup()       

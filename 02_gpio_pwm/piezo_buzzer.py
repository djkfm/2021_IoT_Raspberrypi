# 도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 : 도(262)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle (0~100)

try:
    time.sleep(2)
    pwm.ChangeDutyCycle(0)    # 부저음이 나지 않음

finally:
    pwm.stop()
    GPIO.cleanuo()
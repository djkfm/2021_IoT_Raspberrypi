# 도 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 : 도(262)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(50) # duty cycle (0~100)

melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 293, 392, 392, 440, 440, 392, 392, 330, 392, 330, 293, 330, 262]
bit = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4]


try:
    for i in range(len(melody)):
        pwm.ChangeFrequency(melody[i])
        time.sleep(bit[i]*0.5)

finally:
    pwm.stop()
    GPIO.cleanup()
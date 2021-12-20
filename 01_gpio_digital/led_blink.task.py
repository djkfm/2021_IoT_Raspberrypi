import RPi.GPIO as GPIO
import time

LED_PIN_A = 4
LED_PIN_B = 17
LED_PIN_C = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_A, GPIO.OUT)
GPIO.setup(LED_PIN_B, GPIO.OUT)
GPIO.setup(LED_PIN_C, GPIO.OUT)

GPIO.output(LED_PIN_A, GPIO.HIGH)
("led on")
time.sleep(2)
GPIO.output(LED_PIN_A, GPIO.LOW)
("led off")
# time.sleep(2)
GPIO.output(LED_PIN_B, GPIO.HIGH)
("led on")
time.sleep(2)
GPIO.output(LED_PIN_B, GPIO.LOW)
("led off")
# time.sleep(2)
GPIO.output(LED_PIN_C, GPIO.HIGH)
("led on")
time.sleep(2)
GPIO.output(LED_PIN_C, GPIO.LOW)
("led off")
# time.sleep(2)

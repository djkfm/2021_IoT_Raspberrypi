import RPi.GPIO as GPIO

LED_PIN = 4 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        A = input("1:on, 0:off, 9:exit >")
        if A == '0':
            GPIO.output(LED_PIN, GPIO.LOW) # 0
            print("led off")
        elif A == '1':
            GPIO.output(LED_PIN, GPIO.HIGH) # 1
            print("led on")
        elif A == '9':
            break

finally:
    GPIO.cleanup()
    print("cleanup and exit")
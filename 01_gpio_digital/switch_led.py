import RPi.GPIO as GPIO

LED_PIN = 4
SWITCH_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
#누르지 않았을 떄 ; 0, 눌렀을 떄 : 1
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        GPIO.output(LED_PIN, val) 
finally:
    GPIO.cleanup()
    print('cleanup and exit')
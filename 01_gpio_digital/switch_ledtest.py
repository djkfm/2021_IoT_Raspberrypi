import RPi.GPIO as GPIO

R_LED_PIN = 4
R_SWITCH_PIN = 12

Y_LED_PIN = 17
Y_SWITCH_PIN = 16

G_LED_PIN = 27 
G_SWITCH_PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(R_LED_PIN, GPIO.OUT)
GPIO.setup(Y_LED_PIN, GPIO.OUT)
GPIO.setup(G_LED_PIN, GPIO.OUT)
#누르지 않았을 떄 ; 0, 눌렀을 떄 : 1
GPIO.setup(R_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항
GPIO.setup(Y_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(G_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        R_val = GPIO.input(R_SWITCH_PIN)
        Y_val = GPIO.input(Y_SWITCH_PIN)
        G_val = GPIO.input(G_SWITCH_PIN)
        GPIO.output(R_LED_PIN, R_val)
        GPIO.output(G_LED_PIN, G_val)
        GPIO.output(Y_LED_PIN, Y_val) 
finally:
    GPIO.cleanup()
    print('cleanup and exit')
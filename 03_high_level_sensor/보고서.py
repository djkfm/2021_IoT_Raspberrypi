import RPi.GPIO as GPIO
import time
import Adafruit_DHT

BUTTON_PIN = 8
BUZZER_PIN = 2
sensor = Adafruit_DHT.DHT11
PIN = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(BUZZER_PIN, 262)
  

try:
    while True:
        val = GPIO.input(BUTTON_PIN)
        print(val)
        if val == 0:
            humidty, temperature = Adafruit_DHT.read_retry(sensor, PIN)
            if humidty is not None and temperature is not None:
                print(f"Temperature={temperature:.1f}C, Humidty:{humidty:.1f}%")
                if(temperature>=30):
                    pwm.start(50)
                    pwm.ChangeDutyCycle(50)
                else:        
                    pwm.ChangeDutyCycle(0)
            else:
                 print('Good')
            time.sleep(1)
        
finally:
    GPIO.cleanup()
    print("End of Program")
from lcd import drivers
import datetime
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 17
display = drivers.Lcd()

try:
    humidty, temperature = Adafruit_DHT.read_retry(sensor, PIN)
    if humidty is not None and temperature is not None:
        display.lcd_display_string(f"{temperature:.1f}C, {humidty:.1f}%",2)
    else:
        display.lcd_display_string("read error")
    while True:
        now = datetime.datetime.now()
        time.sleep(1)
        display.lcd_display_string(now.strftime("%x%X"),1)
        

        



finally:
    display.ldc_clear()
#dht11.py
import Adafruit_DHT

sensor = Adafruit_DHT.DHT114
DHT_PIN = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print('Temperature=%.1f*, Humidity=%.1f%%' % (t, h))
        else:
            print('read error')

finally:
    print('bye')
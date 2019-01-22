import sys

import Adafruit_DHT

#Setuppaus
sensor = 11
pin = 12

#Senssorin luenta
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#lampotila kelvineina, koska fyysikon on pakko
temperature = temperature + 273

#Tulostus
if humidity is not None and temperature is not None:
    print('Temperature={0:0.1f} K  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    

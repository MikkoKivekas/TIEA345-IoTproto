import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pir = 5

GPIO.setup(pir, GPIO.IN)

while 1:
    i=GPIO.input(pir)
    if i==0:
        print 1
        time.sleep(1)
    elif i==1:
        print 0
        time.sleep(1)

GPIO.cleanup()

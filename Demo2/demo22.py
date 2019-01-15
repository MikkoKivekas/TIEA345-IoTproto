import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pir = 5
nappi = 6

GPIO.setup(pir, GPIO.IN)
GPIO.setup(nappi, GPIO.IN)

while 1:
    i=GPIO.input(pir)
    if i==0:
        print 0
        time.sleep(1)
    elif i==1:
        print 1
        time.sleep(1)
        
    j=GPIO.input(nappi)
    if j==0:
        print "ei nappia"
        time.sleep(1)
    elif j==1:
        print "nappi"
        time.sleep(1)

GPIO.cleanup()

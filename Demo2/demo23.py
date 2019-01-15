
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


green =16
yellow = 20
red = 21
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

stop =6
go = 5
GPIO.setup(stop, GPIO.OUT)
GPIO.setup(go, GPIO.OUT)

mark = 19
GPIO.setup(mark, GPIO.OUT)

button = 26
pir = 22
GPIO.setup(button, GPIO.IN)
GPIO.setup(pir, GPIO.IN)

GPIO.output(red, 1) #for testing

while True:
    if GPIO.output(green,1)==1:
        GPIO.output(yellow, 1)
        GPIO.output(green, 0)
        time.sleep(1)
        GPIO.output(red, 1)
        GPIO.output(yellow, 0)
        time.sleep(1)
        
    if GPIO.output(red,1)==1:
        GPIO.output(yellow, 1)
        time.sleep(1)
        GPIO.output(green, 1)
        GPIO.output(yellow, 0)
        GPIO.output(red, 0)
        time.sleep(1)
        
GPIO.cleanup()

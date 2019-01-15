
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

#initial condition
GPIO.output(red, 0) 
GPIO.output(green, 1)
GPIO.output(yellow, 0)
GPIO.output(go, 0)
GPIO.output(stop, 1)
time.sleep(3)

isGreen = 1
j = 1

def carlights(i):
    if i==1:
        GPIO.output(yellow, 1)
        GPIO.output(green, 0)
        time.sleep(1)
        GPIO.output(red, 1)
        GPIO.output(yellow, 0)
        isGreen = 0
        time.sleep(1)
        
    if i==0:
        GPIO.output(yellow, 1)
        time.sleep(1)
        GPIO.output(green, 1)
        isGreen = 1
        GPIO.output(yellow, 0)
        GPIO.output(red, 0)
        time.sleep(1)
    
    return isGreen
    
    
while j == 1:   
    if GPIO.input(button) ==1:
        GPIO.output(mark, 1)
        if GPIO.input(pir)==1:
            time.sleep(2)
        isGreen = carlights(isGreen)#vaihtaa autojen valot v>p
        GPIO.output(mark, 0)
        GPIO.output(go, 1)
        GPIO.output(stop, 0)
        time.sleep(3)
        GPIO.output(stop, 1)
        GPIO.output(go, 0)
        time.sleep(1)
        isGreen = carlights(isGreen)#vaihtaa autojen valot p>v
        time.sleep(3)
        j = 0
    
        
GPIO.cleanup()

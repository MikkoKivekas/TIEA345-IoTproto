from picamera import PiCamera
import system as sys
import RPi.GPIO as GPIO
import time

camera = PiCamera()
pir = 4
GPIO.setup(pir, GPIO.IN)

i = 1

while i:
  time.sleep(0.5)
  if GPIO.input(pir)==1:
    camera.start_preview()
    camera.capture('/home/pi/IoT/TIEA345/Demo3/pir.jpg')
    camera.stop_preview()
    time.sleep(1)
    i = 0
   
GPIO.cleanup()

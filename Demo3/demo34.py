from picamera import PiCamera
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

camera = PiCamera()
pir = 4
GPIO.setup(pir, GPIO.IN)

i = 1
time.sleep(7) 
while i:
  time.sleep(0.5)
  if GPIO.input(pir)==1:
    camera.start_preview()
    camera.capture('/home/pi/IoT/TIEA345/Demo3/pir.jpg')
    camera.stop_preview()
    time.sleep(1)
    i = 0
   
GPIO.cleanup()

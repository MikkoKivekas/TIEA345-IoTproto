import RPi.GPIO as GPIO
import time

Vilkku = 4

GPIO.clenaup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(Vilkku, GPIO.OUT)

for x in range(0, 3):
    GPIO.output(Vilkku, 1)
    time.sleep(1)
    GPIO.output(Vilkku, 0)
    time.sleep(1)



GPIO.cleanup()

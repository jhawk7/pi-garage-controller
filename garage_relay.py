import RPi.GPIO as GPIO #using RPi.GPIO for pi zero
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class GarageRelay:
  def __init__(self, pin):
    GPIO.setup(pin, GPIO.OUT)
    self.relay = pin
  
  def trigger(self):
    GPIO.output(self.relay,GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(self.relay,GPIO.LOW)

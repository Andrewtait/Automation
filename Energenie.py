
import RPi.GPIO as GPIO
import time

class Energenie():
  def gpiosetup(self):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(22,GPIO.OUT)
    GPIO.output(22,False)
    GPIO.output(18,False)
    GPIO.output(11,False)
    GPIO.output(15,False)
    GPIO.output(16,False)
    GPIO.output(13,False)

  def gpioon(self):
    GPIO.output(11,True)
    GPIO.output(15,True)
    GPIO.output(16,False)
    GPIO.output(13,True)
    time.sleep(0.1)
    GPIO.output(22,True)
    time.sleep(0.25)
    GPIO.output(22,False)

  def gpiooff(self):
    GPIO.output(11,True)
    GPIO.output(15,True)
    GPIO.output(16,False)
    GPIO.output(13,False)
    time.sleep(0.1)
    GPIO.output(22,True)
    time.sleep(0.25)
    GPIO.output(22,False)

  def gpiocleanup(self):
    GPIO.cleanup()

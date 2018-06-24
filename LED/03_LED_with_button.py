#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11 # pin11
ButtonPin = 13

def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LedPin, GPIO.OUT)
  GPIO.output(LedPin, GPIO.LOW)

def loop():
    while True:
      if GPIO.input(ButtonPin) == 1:
          print '...led on'
          GPIO.output(LedPin, GPIO.HIGH) # turn led on
          time.sleep(0.05)
          if GPIO.input(ButtonPin) == 0:
            print '...led off'
            GPIO.output(LedPin, GPIO.LOW) # rutn led on

def destroy():
  GPIO.output(LedPin, GPIO.HIGH) # led off
  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()

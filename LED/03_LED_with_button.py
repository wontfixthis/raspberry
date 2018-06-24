#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11 # pin11
ButtonPin = 13
Warten = 0.04

def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  #GPIO.setup(LedPin, GPIO.OUT)
  #GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():
  while True:
    print '...led on'
    time.sleep(Warten)
    GPIO.output(LedPin, GPIO.LOW) # led on time.sleep(0.5)
    time.sleep(Warten)
    print 'led off...'
    print GPIO.input(ButtonPin)
    GPIO.output(LedPin, GPIO.HIGH) # led off time.sleep(0.5)
    #time.sleep(1)

def destroy():
  GPIO.output(LedPin, GPIO.HIGH) # led off
  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    destroy()


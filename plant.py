#!/usr/bin/python 
import RPi.GPIO as GPIO

# set up the GPIO channels - one input and one output
GPIO.setup(16, GPIO.IN)
GPIO.setup(12, GPIO.OUT)

# input from pin 16 
input_value = GPIO.input(16)

print(input_value)

# output to pin 12
GPIO.output(12, True)


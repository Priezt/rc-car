#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Wheel:
    def __init__(pin0, pin1):
        self.pin0 = pin0
        self.pin1 = pin1
        GPIO.setup(pin0, GPIO.OUT)
        GPIO.setup(pin1, GPIO.OUT)

    def forward(t):
        GPIO.output(self.pin0, GPIO.HIGH)
        GPIO.output(self.pin1, GPIO.LOW)
        time.sleep(t)
        GPIO.output(self.pin0, GPIO.LOW)
        GPIO.output(self.pin1, GPIO.LOW)
        
    def backward(t):
        GPIO.output(self.pin0, GPIO.LOW)
        GPIO.output(self.pin1, GPIO.HIGH)
        time.sleep(t)
        GPIO.output(self.pin0, GPIO.LOW)
        GPIO.output(self.pin1, GPIO.LOW)
        
class Car:
    def __init__(left_wheel, right_wheel):
        self.left_wheel = left_wheel
        self.right_wheel = right_wheel

    def forward(t):
        self.left_wheel.forward(t)
        self.right_wheel.forward(t)

car(Wheel(21, 20), Wheel(16, 12))
car.forward(1)

GPIO.cleanup()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import tty, sys, termios

GPIO.setmode(GPIO.BCM)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class Wheel:
    def __init__(self, pin0, pin1):
        self.pin0 = pin0
        self.pin1 = pin1
        GPIO.setup(pin0, GPIO.OUT)
        GPIO.setup(pin1, GPIO.OUT)

    def forward(self):
        GPIO.output(self.pin0, GPIO.HIGH)
        GPIO.output(self.pin1, GPIO.LOW)

    def stop(self):
        GPIO.output(self.pin0, GPIO.LOW)
        GPIO.output(self.pin1, GPIO.LOW)
        
    def backward(self):
        GPIO.output(self.pin0, GPIO.LOW)
        GPIO.output(self.pin1, GPIO.HIGH)
        
class Car:
    def __init__(self, left_wheel, right_wheel):
        self.left_wheel = left_wheel
        self.right_wheel = right_wheel

    def forward(self, t):
        self.left_wheel.forward()
        self.right_wheel.forward()
        time.sleep(t)
        self.left_wheel.stop()
        self.right_wheel.stop()

    def backward(self, t):
        self.left_wheel.backward()
        self.right_wheel.backward()
        time.sleep(t)
        self.left_wheel.stop()
        self.right_wheel.stop()

    def turn_left(self, t):
        self.right_wheel.forward()
        time.sleep(t)
        self.right_wheel.stop()

    def turn_right(self, t):
        self.left_wheel.forward()
        time.sleep(t)
        self.left_wheel.stop()

car = Car(Wheel(16, 12), Wheel(21, 20))

while(True):
    char = getch()
    keycode = ord(char)
    if keycode == 113:
        break
    elif keycode == 65:
        print "forward"
        car.forward(1)
    elif keycode == 66:
        print "backward"
        car.backward(1)
    elif keycode == 68:
        print "turn left"
        car.turn_left(0.2)
    elif keycode == 67:
        print "turn right"
        car.turn_right(0.2)

GPIO.cleanup()

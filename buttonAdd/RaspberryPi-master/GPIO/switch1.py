#!/usr/bin/python
import RPi.GPIO as GPIO
import time

switch = 18  # GPIO18
delay = 0.2  # 0.2 seconds
GPIO.setwarnings(False)  # disable warnings
GPIO.setmode(GPIO.BCM)  # mode BCM or Board
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # input or output
isRunning = True
while isRunning:
    try:
        input_state = GPIO.input(switch)
        if not input_state:
            print("Button Pressed")
        time.sleep(delay)
    except KeyboardInterrupt:
        isRunning = False
GPIO.cleanup()

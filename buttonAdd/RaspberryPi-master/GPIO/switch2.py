#!/usr/bin/python
import RPi.GPIO as GPIO
import time

led = 18  # GPIO18
switch = 23
GPIO.setwarnings(False)  # disable warnings
GPIO.setmode(GPIO.BCM)  # mode BCM or Board
GPIO.setup(led, GPIO.OUT)  # input or output
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
led_state = False
old_input_state = True
isRunning = True
while isRunning:
    try:
        new_input_state = GPIO.input(switch)
        if not new_input_state and old_input_state:
            led_state = not led_state
        old_input_state = new_input_state
        GPIO.output(led, led_state)
    except KeyboardInterrupt:
        isRunning = False
GPIO.cleanup()

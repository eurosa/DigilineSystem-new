from Tkinter import *
import RPi.GPIO as GPIO
import time


class App:
    def __init__(self, master):
        frame = Frame(master)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        pwm = GPIO.PWM(18, 100)
        pwm.start(5)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)

    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)

    def __exit__(self, exc_type, exc_val, exc_tb):
        GPIO.cleanup()


root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()

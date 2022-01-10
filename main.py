import os

os.environ['DISPLAY'] = ":0.0"
os.environ['KIVY_WINDOW'] = 'egl_rpi'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from pidev.MixPanel import MixPanel
from pidev.kivy.PassCodeScreen import PassCodeScreen
from pidev.kivy.PauseScreen import PauseScreen
from pidev.kivy import DPEAButton
from pidev.kivy import ImageButton
from pidev.kivy.selfupdatinglabel import SelfUpdatingLabel
from kivy.properties import ObjectProperty
from kivy.animation import Animation

from datetime import datetime
from kivy.uix.widget import Widget
from threading import Thread
from time import sleep
time = datetime

SCREEN_MANAGER = ScreenManager()
MAIN_SCREEN_NAME = 'main'
ADMIN_SCREEN_NAME = 'admin'



import spidev
import RPi.GPIO as GPIO
from pidev.stepper import stepper
from Slush.Devices import L6470Registers
spi = spidev.SpiDev()
s0 = stepper(port=0, micro_steps=32, hold_current=20, run_current=20, accel_current=20, deaccel_current=20,
             steps_per_unit=200, speed=2)

class ProjectNameGUI(App):

    def build(self):
        return SCREEN_MANAGER
Window.clearcolor = (1, 1, 1, 1)


class MainScreen(Screen):
    def start_stepper(self):
        s0.go_until_press(0,self.cute_slider.value*6400)
    def change(self):
        s0.go_until_press(1, self.cute_slider.value*6400)
    def slider_speed(self):
        self.cute_slider
        self.mcqueen_label
        s0.set_speed(self.cute_slider.value)
    def shy(self):
        self.i_get_position.text = str(-s0.get_position_in_units())
        s0.set_speed(1)
        s0.start_relative_move(-15)
        while s0.isBusy():
            sleep (1)
        self.i_get_position.text = str(-s0.get_position_in_units())
        sleep(10)
        s0.set_speed(5)
        s0.start_relative_move(-10)
        sleep(8)
        s0.goHome()
        self.i_get_position.text = str(-s0.get_position_in_units())
        sleep(30)
        s0.set_speed(8)
        s0.start_relative_move(100)
        while s0.isBusy():
            sleep(1)
        self.i_get_position.text = str(-s0.get_position_in_units())
        sleep (10)
        s0.goHome()
        while s0.isBusy():
            sleep(1)
        self.i_get_position.text = str(-s0.get_position_in_units())




    def shy_thread(self):
        Thread(target=self.shy, daemon = True).start()





    def stop_stepper(self):
        s0.softStop()



Builder.load_file('main.kv')
SCREEN_MANAGER.add_widget(MainScreen(name=MAIN_SCREEN_NAME))

#


def send_event(event_name):

    global MIXPANEL

    MIXPANEL.set_event_name(event_name)
    MIXPANEL.send_event()


if __name__ == "__main__":
    # send_event("Project Initialized")
    # Window.fullscreen = 'auto'
    ProjectNameGUI().run()

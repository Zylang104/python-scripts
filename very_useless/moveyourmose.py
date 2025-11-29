import pyautogui
import random
import keyboard
pyautogui.FAILSAFE=False
running=True
def stop():
    global running
    running=False
keyboard.add_hotkey('delete',stop)
def move():
    global running
    print("Starting fast, random mouse movement. Press 'Delete' to stop.")
    w,h=pyautogui.size()
    while running:
        pyautogui.moveTo(random.randint(0,w-1),random.randint(0,h-1),duration=0.05)
    print("Mouse movement stopped.")
move()
from pyautogui import *
from time import sleep
import keyboard
import sys
from timer import Timer
import time
import win32api, win32con
from threading import Thread
from monitor import *
from reel import *

window = getWindowsWithTitle("Russian Fishing 4")[0]
window.activate()

sleep(1)

test_reel = Narga8000()
for i in range(5):
    # test_reel.twitching()
    # test_reel.walk_the_dog()
    test_reel.jig_step()
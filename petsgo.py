from PIL import Image
import mss
import pynput
import pyautogui
import sys
import math

#do pip3 install PIL 
#and pip3 install mss
#and pip3 install pynput
#and pip3 install pyautogui


keys = pynput.keyboard.Controller()
freq = 7
pyautogui.FAILSAFE = False
gathering = False
def swap(): 
    global gathering
    gathering = not(gathering)
listener = pynput.keyboard.GlobalHotKeys({'o+p': swap})
listener.start()
import time
def screenshot():
    im = ''
    while im == '':
        with mss.mss() as sct:
            try:
                monitor = sct.monitors[1]
                sct_img = sct.grab(monitor)
                im = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            except: pass
    return im
def keypress(delay,key,key2='none',key3='none',checkhaste=False):
    if delay > 0.08:
        if key != 'none': keys.press(key)
        if key2 != 'none': keys.press(key2)
        if key3 != 'none': keys.press(key3)
        time.sleep(delay)
        if key != 'none': keys.release(key)
        if key2 != 'none': keys.release(key2)
        if key3 != 'none': keys.release(key3)
    elif delay == 0.08:
        keys.press(key)
        time.sleep(0.08)
        keys.release(key)
    else:
        keys.press(key)
        keys.release(key)
coin = time.time()
clickx, clicky = 1000,1000
lastmoved = time.time()
def breakcoin(x,y):
    global lastmoved
    global coin
    global clickx
    global clicky
    if time.time()-lastmoved > 8:
        keypress(6,'s',pynput.keyboard.Key.space)
    if (abs(clickx-x)**2 + abs(clicky-y)**2)**0.5 > 100:
        pyautogui.rightClick(x,y)
        lastmoved = time.time()
    else:
        pyautogui.click(clickx,clicky)
    clickx,clicky = x,y
    coin = time.time()
im = screenshot()
width,height = im.size
def scan(x,y,im):
    global width
    global height
    if y > 666 and y < 1332 and x < 444: return
    elif y > 1440: return
    if x >= width-freq or x <= freq: return True
    if y >= height-freq or y <= freq: return
    else:
        coins = [(250, 228, 76), (250, 227, 76), (250, 225, 75), (250, 223, 75), (250, 226, 76), (251, 230, 77), (251, 232, 77), (251, 231, 77), (251, 234, 78), (251, 235, 78), (251, 233, 78), (252, 237, 79), (252, 236, 79), (252, 238, 79), (250, 224, 75), (249, 222, 75), (249, 218, 73), (249, 220, 74)]
        (r,g,b) = im.getpixel((x,y))
        if (r,g,b) in coins:
            print('e')
            breakcoin(math.floor(x/2),math.floor(y/2))
            return  True
def searchitems():
    im = screenshot()
    exit = False
    x,y = math.floor(width/2), math.floor(height/2)
    rotate = 0
    step = 0.5
    while exit == False:
        step = step + 0.5
        if rotate < 3:
            rotate = rotate + 1
        else:
            rotate = 0
        if rotate == 0:
            newval = y - math.floor(step)*freq
            while y > newval:
                y=y-freq
                if scan(x,y,im) == True:
                    exit = True
        if rotate == 1:
            newval = x - math.floor(step)*freq
            while x > newval:
                x=x-freq
                if scan(x,y,im) == True:
                    exit = True
        if rotate == 2:
            newval = y + math.floor(step)*freq
            while y < newval:
                y=y+freq
                if scan(x,y,im) == True:
                    exit = True
        if rotate == 3:
            newval = x + math.floor(step)*freq
            while x < newval:
                x=x+freq
                if scan(x,y,im) == True:
                    exit = True
vending = time.time()-661
cycle = 0
time.sleep(1)
def gotovending():
    global lastmoved
    keypress(0.08,'q')
    keypress(5,'s')
    keypress(0.08,'q')
    keypress(5,'s',pynput.keyboard.Key.space)
    keypress(0.08,'q')
    keypress(8,'w')
    keypress(0.08,'q')
    keypress(8,'w')
    keypress(0.1,'s')
    keypress(0.08,pynput.keyboard.Key.space)
    keypress(2,'w')
    keypress(2.5,'w','d')
    keypress(0.5,'s','a')
    for i in range(5):
        time.sleep(2)
        pyautogui.click(570*width/2880,625*height/1800)
    time.sleep(1)
    pyautogui.click(720*width/2880,620*height/1800)
    keypress(9,'s',pynput.keyboard.Key.space)
    lastmoved = time.time()
while True:
    if gathering:
        if time.time()-vending > 660:
            gotovending()
            vending = time.time()
        else:
            if coin < time.time()-1:
                cycle = cycle + 1
                if cycle > 22:
                    cycle = 1
                if cycle in [1,8,9,18]:
                    keypress(0.7,'d')
                if cycle in [2,7,12,13,19]:
                    keypress(0.7,'w')
                if cycle in [3,6,11,14,20]:
                    keypress(0.7,'a')
                if cycle in [4,5,10,15]:
                    keypress(0.7,'s')
                if cycle in [16,22]:
                    keypress(0.35,'d')
                if cycle in [17,21]:
                    keypress(0.35*2,'s')
            searchitems()

#yes, this pattern is snaildance v3 from bee swarm simulator xd

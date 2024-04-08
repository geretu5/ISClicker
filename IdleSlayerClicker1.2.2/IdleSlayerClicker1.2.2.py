import pyautogui
from time import sleep
import keyboard

pyautogui.PAUSE = 0.02
pyautogui.FAILSAFE = False

x = 0
y = 0
counter = 0
ss = 1
craft=0
MinionsMas = ['Scelet.png', 'WhiteKnight.png', 'JijaMutant.png', 'DarkWizard.png', 'StoneGolem.png', 'Ninja.png']

def move():
    pyautogui.click(1070, 980)
    pyautogui.click(950, 20)
    pyautogui.click(1070, 850)
    pyautogui.click(1635, 175)
    for i in range(5):
        pyautogui.click(5, 5)

def slides():
    if (pyautogui.locateCenterOnScreen('SliderToLeft.png', confidence=0.7, region=(0,0, 1920, 1080))):
        x, y = pyautogui.locateCenterOnScreen('SliderToLeft.png', confidence=0.7, region=(0,0, 1920, 1080))
        pyautogui.moveTo(x, y)
        pyautogui.dragTo(695, y, duration=1)
    elif (pyautogui.locateCenterOnScreen('SliderToRight.png', confidence=0.7, region=(0,0, 1920, 1080))):
        x, y = pyautogui.locateCenterOnScreen('SliderToRight.png', confidence=0.7, region=(0,0, 1920, 1080))
        pyautogui.moveTo(x, y)
        pyautogui.dragTo(1225, y, duration=1)

def crafting():
    global craft
    pyautogui.click(1870, 550)

def eggs():
    pyautogui.click(260,110)
    sleep(0.1)
    pyautogui.click(390, 990)
    pyautogui.click(720, 560)
    for i in range(100):
        pyautogui.click(610, 755)
        pyautogui.click(975, 845)

def BasicChest():
    x, y = pyautogui.locateCenterOnScreen('Chest.png', confidence=0.9, region=(0,0, 1920, 1080))
    pyautogui.click(x, y)

def ShieldChest():
    x, y = pyautogui.locateCenterOnScreen('ShieldChest.png', confidence=0.9, region=(0,0, 1920, 1080))
    pyautogui.click(x, y)

def PerfectChest():
    x, y = pyautogui.locateCenterOnScreen('PerfectChest.png', confidence=0.8, region=(0, 0, 1920, 1080))
    pyautogui.click(x, y)

def chests():
    if(pyautogui.locateCenterOnScreen('ShieldChest.png', confidence=0.9, region=(0,0, 1920, 1080))):
        sleep(2)
        BasicChest()
        sleep(2)
        BasicChest()
        sleep(2)
        ShieldChest()
        while True:
            if(pyautogui.locateCenterOnScreen('Chest.png', confidence=0.9, region=(0,0, 1920, 1080))):
                try:
                    BasicChest()
                    sleep(1)
                except:
                    pass
            else:
                break
        try:
            sleep(10)
            PerfectChest()
        except:
            pass

def minionsCollect():
    x, y = pyautogui.locateCenterOnScreen('MinionsCollect.png', confidence=0.7, region=(0, 0, 1920, 1080))
    pyautogui.click(x, y)
    pyautogui.moveTo(0, 0)
    sleep(0.5)
    x, y = pyautogui.locateCenterOnScreen('MinionsSendMission.png', confidence=0.6, region=(0, 0, 1920, 1080))
    pyautogui.click(x, y)
    pyautogui.moveTo(0, 0)
    sleep(0.5)

def GodPoints():
    pyautogui.moveTo(900, 900)
    pyautogui.dragTo(900, 400, duration=0.3)
    for b in range(2):
        for c in range(3):
            try:
                if (pyautogui.locateCenterOnScreen(MinionsMas[c+b*3], confidence=0.9, region=(0, 0, 1920, 1080))):
                    x, y = pyautogui.locateCenterOnScreen(MinionsMas[c+b*3], confidence=0.9, region=(0, 0, 1920, 1080))
                    pyautogui.click(x + 100, y - 10)
                    sleep(0.2)
                    pyautogui.click(830, 830)
                    sleep(0.4)
                    pyautogui.click(500, 230)
            except:
                pass
        pyautogui.moveTo(900, 400)
        pyautogui.dragTo(900, 700, duration=0.3)

def minions():
    if (pyautogui.locateCenterOnScreen('Minions.png', confidence=0.99, region=(0, 0, 1920, 1080))):
        pyautogui.click(150, 110)
        sleep(0.5)
        pyautogui.click(480, 995)
        sleep(0.5)
        if (pyautogui.locateCenterOnScreen('MinionsDailyBonus.png', confidence=0.7, region=(0, 0, 1920, 1080))):
            try:
                minionsCollect()
                x, y = pyautogui.locateCenterOnScreen('MinionsDailyBonus.png', confidence=0.7, region=(0, 0, 1920, 1080))
                pyautogui.click(x, y)
                sleep(0.5)
                pyautogui.moveTo(0, 0)
                minionsCollect()
            except:
                pass
        elif (pyautogui.locateCenterOnScreen('MinionsCollect.png', confidence=0.7, region=(0, 0, 1920, 1080))):
            try:
                minionsCollect()
            except:
                pass
        GodPoints()
        pyautogui.click(840, 990)

while True:
    craft=0
    if (keyboard.is_pressed('f1')):
        while True:
            pyautogui.rightClick(1920 / 2, 1080 / 2)
            move()
            if(counter == 6):
                chests()
                slides()
                minions()
                counter = 0
            counter += 1
            if (craft>1):
                crafting()
            if (keyboard.is_pressed('f3')):
                craft += 1
            if (keyboard.is_pressed('f2')):
                break
    if (keyboard.is_pressed('f4')):
        eggs()

#ctrl alt shift j <---- имитируем и двигаем курсор

#pyautogui - управление мышью
#keyboard - считывание клавиш с клавиатуры


#сделать макрос для update readme
#добавить проверку активного окна ворд


import keyboard
import pyautogui
import time
import ctypes


def get_language():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        return 'ru'
    if hex(pf(0)) == '0x4090409':
        return 'en'
'''   
if get_language() == "ru":
    print("изменение расскладки на инглиш")
    
    pyautogui.hotkey('alt', 'shift')
    time.sleep(1)
'''   
def changingPharagraph():
    cursorX, cursorY = pyautogui.position()

    offSetX = -120 #данные нужно подогнать под себя
    offSetY = 35
    global wordHotKey
    
    keyboard.press(29)  # Ctrl
    keyboard.press(42)  # Shift
    keyboard.press(56)  # Alt
    keyboard.press(36)  # J

    keyboard.release(36)  # J
    keyboard.release(56)  # Alt
    keyboard.release(42)  # Shift
    keyboard.release(29)  # Ctrl
    pyautogui.moveTo(1920/2 + offSetX, 1080/2+offSetY)
    pyautogui.doubleClick() 

    keyboard.send("ctrl+a")
    keyboard.write("0")
    keyboard.send("enter")

    pyautogui.moveTo(cursorX, cursorY)
    print("макрос успешно выполнен")
    

programm = True

myHotKey = 'alt+m'
wordHotKey = 'ctrl+shift+alt+j'


keyboard.add_hotkey(myHotKey, changingPharagraph)

while programm:
    command = input()
    if command == "exit":
        programm = False


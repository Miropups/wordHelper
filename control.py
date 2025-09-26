#ctrl alt shift j <---- имитируем и двигаем курсор

#pyautogui - управление мышью
#keyboard - считывание клавиш с клавиатуры

import keyboard
import pyautogui



def changingPharagraph():
    offSetX = -120 #данные нужно подогнать под себя
    offSetY = 35
    global wordHotKey
    
    keyboard.send(wordHotKey)

    pyautogui.moveTo(1920/2 + offSetX, 1080/2+offSetY)
    pyautogui.doubleClick() 

    keyboard.send("ctrl+a")
    keyboard.write("0")
    keyboard.send("enter")

    print("макрос успешно выполнен")
    

programm = True

myHotKey = 'alt+m'
wordHotKey = 'ctrl+shift+alt+j'


keyboard.add_hotkey(myHotKey, changingPharagraph)

while programm:
    command = input()
    if command == "exit":
        programm = False


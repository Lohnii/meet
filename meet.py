from datetime import datetime
from time import sleep
from random import randrange
from pytesseract import pytesseract
from PIL import Image, ImageGrab, ImageFilter
import pygetwindow as gw
import keyboard
import pyautogui
import win32api, win32con
import cv


####################################################################
#                                   
# Abra uma sala pra testar se ele consegue ler
#
#
navegador = 'chrome' #nome do navegador que vc vai usar
#
####################################################################


# segunda = 0
# terca = 1
# quarta = 2
# quinta = 3
# sexta = 4
# sabado = 5
# domingo = 6

# links -> atualizar no options.txt
aulaSegunda = ''
aulaTerca = ''
aulaQuarta = ''
aulaQuinta = ''
aulaSexta = ''
aulaSabado = ''
aulaDomingo = ''

linkDict = {0: aulaSegunda, 1: aulaTerca, 2: aulaQuarta, 3: aulaQuinta, 4: aulaSexta, 5: aulaSabado, 6: aulaDomingo}

keyword = 'presente'
keywordTimes = 4 #quantas vezes tem que aparecer

global pathToTesseract
pathToTesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def Sleep(time = 1):
    r = randrange(100,200)/100
    sleep(time+r)

def GetTodaysLink():
    weekday = datetime.today().weekday()
    print(linkDict[weekday])
    return linkDict[weekday]

def ReadChat():
    img = ImageGrab.grab(include_layered_windows=False, all_screens=True)
    # img = ImageGrab.grab(include_layered_windows=False)
    #resize image
    newHeight = img.height *2
    newWidth = img.width * 2
    img = img.resize((newWidth, newHeight),Image.Resampling.LANCZOS)
    img = img.filter(ImageFilter.SMOOTH)
    # img.show()
    img = cv.CleanImage(img.convert('RGB'))

    pytesseract.tesseract_cmd = pathToTesseract

    #extract text from image
    text = pytesseract.image_to_string(img, config='tessedit_char_whitelist=0123456789').lower()
    print(text)
    return text

def LookForKeyword():
    while True:
        txt = ReadChat()
        txt = txt.split()
        
        # c = txt.count('presente')
        c = 0
        for i in txt:
            if 'presente' in i:
                c += 1

        print(f'count = {c}')

        if c >= 4:
            return True

        Sleep(3)

def Browser():
    #procura e abre a janela
    window = gw.getWindowsWithTitle(navegador)[0]
    print(window)
    window.restore()
    window.maximize()
    window.activate()

    #entra no site
    keyboard.press_and_release('f6')
    Sleep(0.5)
    keyboard.write(GetTodaysLink())
    Sleep(0.5)
    keyboard.press_and_release('enter')

def Click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    Sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    Sleep(0.1)

def ClickPos(pos):
    win32api.SetCursorPos((pos[0],pos[1]))
    Sleep(0.1)
    Click()

def Entra():
    # #procura o botao participar
    botao = 'participar.png'
    x = 0
    y = 0
    print('procurando', botao)

    achou = False
    while achou == False:
        try:
            b = list(pyautogui.locateAllOnScreen(botao))
            if b != None:
                x, y = pyautogui.center(b[-1])
                achou = True
                
                #clica
                # win32api.SetCursorPos((x,y))
                ClickPos([x,y+3])
        except Exception as e:
            print(e)
        sleep(0.5)
                
def LookForChat():
    # #procura o chat
    botao = 'chat.png'
    x = 0
    y = 0
    print('procurando', botao)

    achou = False
    while achou == False:
        try:
            b = list(pyautogui.locateAllOnScreen(botao))
            if b != None:
                x, y = pyautogui.center(b[-1])
                achou = True

                y += 10

                #clica
                # win32api.SetCursorPos((x,y))
                ClickPos([x,y+3])
        except Exception as e:
            # print(f'{e} <- nao tem problema se der erro aqui geralmente')
            pass
        sleep(0.5)

def MaximizeTab():
    w = gw.getWindowsWithTitle('meet:')
    for i in range(len(w)):
        print(w[i])

    w = w[0]
    w.moveTo(10,10)
    sleep(1)
    w.maximize()
    w.activate()

def Presente():
    print('presente', datetime.now())
    Sleep(0.5)
    keyboard.write('presente')
    Sleep(0.3)
    keyboard.press_and_release('enter')
    Sleep(0.1)

    #salva a imagem do presente pra vc ver se/quando funcionou
    img = ImageGrab.grab(include_layered_windows=False, all_screens=True)
    img.save('img.png')
    

def Main():
    # Browser()
    # Entra()
    if LookForKeyword():
        MaximizeTab()
        LookForChat()
        Presente()


if __name__ == '__main__':
    Main()
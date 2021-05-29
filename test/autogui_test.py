import pyautogui
import win32gui
import time



hwnd = win32gui.FindWindow(None, '微信')
print(hwnd)

if(win32gui.IsIconic(hwnd)):#如果最小化则激活并展示
    win32gui.ShowWindow(hwnd, 9)
    time.sleep(0.5)

win32gui.SetForegroundWindow(hwnd)  #展示到最前


img_location = pyautogui.locateOnScreen(image='img.png')

if img_location:
    x, y = pyautogui.center(img_location)
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()

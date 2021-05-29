import pyautogui
import win32gui



hwnd = win32gui.FindWindow(None, '微信')
print(hwnd)
win32gui.SetForegroundWindow(hwnd)


img_location = pyautogui.locateOnScreen(image='img.png')

if img_location:
    x, y = pyautogui.center(img_location)
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()

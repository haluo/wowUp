import pyautogui
import win32gui
import time



hwnd = win32gui.FindWindow(None, '战网')
print(hwnd)

if(win32gui.IsIconic(hwnd)):#如果最小化则激活并展示
    win32gui.ShowWindow(hwnd, 9)
    time.sleep(0.5)

win32gui.SetForegroundWindow(hwnd)  #展示到最前


img_location = pyautogui.locateOnScreen(image='res/bn_login_btn.png')

if img_location:
    print("点击登录按钮")
    x, y = pyautogui.center(img_location)
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
else:
    print("未找到登录按钮")
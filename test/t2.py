import win32api,win32con,win32gui
import time

def get_window_pos(name):
    handle = win32gui.FindWindow(0,name)
    if handle == 0:
        return None
    else:
        #恢复应用窗口到最大化及置顶
        win32gui.SendMessage(handle,win32con.WM_SYSCOMMAND,win32con.SC_RESTORE,0)
        win32gui.SetForegroundWindow(handle)
        return win32gui.GetWindowRect(handle),handle
(x1,y1,x2,y2),handle = get_window_pos('钉钉')
from PIL import Image, ImageGrab
#print(x1,y1,x2,y2)

#等待应用刷新页面
time.sleep(3)
#按应用的尺寸截图
img = ImageGrab.grab((x1,y1,x2,y2))
#保存截图
img.save(r'capture.jpg','jpeg')

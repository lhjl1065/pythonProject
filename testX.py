import time

import cv2
import numpy as np
import pyautogui
from PIL import Image

class ImageNotFoundException(Exception):
    pass

def screenshot():
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    return screen

def find_image(screenshot, target_image_path, threshold=0.86):
    target_image = cv2.imread(target_image_path)
    template_height = target_image.shape[0]
    template_width = target_image.shape[0]
    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    gray_target_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_screenshot, gray_target_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > threshold:
        if 1571 > max_loc[0] > 1565 and 1107 > max_loc[1] > 1103:
            print("疲劳值为0，即将切换角色")
            return True
        if 1804 > max_loc[0] > 1800 and 606 > max_loc[1] > 602:
            print("副本失败，即将切换角色")
            return True
    return False
    # result[max_loc[1]:max_loc[1] + template_height, max_loc[0]:max_loc[0] + template_width] = 0
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# 示例用法
def find_image_method():
    time.sleep(3)
    target_image_path1 = r"C:\Users\Administrator\Pictures\dnf\ZEROPL.png"  # 请确保此处设置了正确的目标图像文件路径

    # 截取屏幕
    screen = screenshot()

    # 在屏幕截图中找到目标图像1和图像2，并计算它们Y轴最大值之差
    result = find_image(screen, target_image_path1)
    print(result)
    return result

find_image_method()

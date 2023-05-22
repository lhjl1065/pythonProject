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

def find_image(screenshot, target_image_path, threshold=0.4):
    target_image = cv2.imread(target_image_path)

    gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    gray_target_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(gray_screenshot, gray_target_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val < threshold:
        raise ImageNotFoundException(f"未找到目标图像: {target_image_path}")

    top_left = max_loc
    y_max = top_left[1] + target_image.shape[0]  # 获取Y轴最大值

    return y_max

# 示例用法
target_image_path1 = r"C:\Users\Administrator\Pictures\ZHAOHUAN.png"  # 请确保此处设置了正确的目标图像文件路径
target_image_path2 = r"C:\Users\Administrator\Pictures\HALO.png"  # 请确保此处设置了正确的目标图像文件路径

# 截取屏幕
screen = screenshot()

# 在屏幕截图中找到目标图像1和图像2，并计算它们Y轴最大值之差
try:
    y_max1 = find_image(screen, target_image_path1)
    print(f"图像1 Y轴最大值：{y_max1}")
except ImageNotFoundException as e:
    print(e)

try:
    y_max2 = find_image(screen, target_image_path2)
    print(f"图像2 Y轴最大值：{y_max2}")
except ImageNotFoundException as e:
    print(e)

if 'y_max1' in locals() and 'y_max2' in locals():
    difference = y_max1 - (y_max2-22)
    print(f"Y轴最大值之差：{difference}")
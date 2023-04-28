import os
import time

import cv2
import numpy as np
import pyautogui
import pytesseract
import re
from PIL import Image

def screenshot_region(top_left, bottom_right):
    x1, y1 = top_left
    x2, y2 = bottom_right
    width = x2 - x1
    height = y2 - y1

    region = (x1, y1, width, height)
    screenshot = pyautogui.screenshot(region=region)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    return screenshot

def process_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    return binary_image

def ocr_image(image):
    text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    numbers = [int(match) for match in re.findall(r'\d+', text)]

    for number in numbers:
        if 0 <= number <= 188:
            return number

    return 999

def extract_number(top_left, bottom_right):
    region_image = screenshot_region(top_left, bottom_right)
    processed_image = process_image(region_image)
    cv2.imwrite('temp_ocr/binary_screenshot.png', processed_image)

    recognized_number = ocr_image(processed_image)
    print("识别出的0到188范围内的数字：")
    print(recognized_number)
    return recognized_number

def extract_number_method():
    time.sleep(3)
    top_left = (1566, 1105)
    bottom_right = (1586, 1119)
    return extract_number(top_left, bottom_right)

extract_number_method()


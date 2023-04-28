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
    return gray_image

def ocr_image(image):
    text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    numbers = [int(match) for match in re.findall(r'\d+', text)]

    for number in numbers:
        if 0 <= number <= 188:
            return number

    return None

def extract_number(top_left_list, bottom_right_list):
    results = []

    for top_left, bottom_right in zip(top_left_list, bottom_right_list):
        region_image = screenshot_region(top_left, bottom_right)
        processed_image = process_image(region_image)
        recognized_number = ocr_image(processed_image)
        results.append(recognized_number)

    valid_results = [result for result in results if result is not None]
    print(valid_results)
    if valid_results:
        max_number = max(valid_results)
        print("识别出的0到188范围内的最大数字：")
        print(max_number)
        return max_number
    else:
        print("无法识别")
        return "999"

def extract_number_method():
    top_left_list = [(1566, 1105), (1566, 1105), (1566, 1105)]
    bottom_right_list = [(1590, 1119), (1584, 1119), (1577, 1119)]
    extract_number(top_left_list, bottom_right_list)

time.sleep(3)
extract_number_method()


from PIL import Image
import pytesseract
import re


# 指定Tesseract OCR的安装路径（仅适用于Windows）
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_image(image_path):
    image = Image.open(image_path)
    # 使用Tesseract OCR提取图像中的数字
    text = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=0123456789')

    # 使用正则表达式查找数字
    numbers = [int(match) for match in re.findall(r'\d+', text)]

    # 查找1到188范围内的数字
    for number in numbers:
        if 1 <= number <= 188:
            return number

    return "未找到1到188范围内的数字"


image_path = r"C:\Users\Administrator\PycharmProjects\pythonDNF\temp_ocr\binary_screenshot.png"  # 替换为您的图像文件路径
recognized_number = ocr_image(image_path)
print("识别出的1到188范围内的数字：")
print(recognized_number)

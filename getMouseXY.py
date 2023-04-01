import pyautogui
import time

# 打印提示信息
print("请将鼠标指向您要双击的位置...")

# 强制程序暂停10秒，以等待用户输入鼠标位置
time.sleep(3)

# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()

# 打印鼠标位置
print(f"鼠标当前位置为 ({currentMouseX}, {currentMouseY})")

# 传送按钮 (808, 1234)
# 点开地图 (1125, 732)
# 选择地图 (868, 155)
# 天界 (809, 233)
# 诺斯匹斯 (1093, 288)
# 地下城入口 (941, 725)
# 确认传送(1114, 732)

import json
import keyboard
import time

import CommonTool

time.sleep(1)
CommonTool.simulate_keyboard_input_from_json("test_speed.json")
print("搬砖完成！")
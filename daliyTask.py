import json
import keyboard
import time

import CommonTool
import pyautogui
import testX


class Character:
    def __init__(self, name, profession, action_points, move_speed):
        self.name = name
        self.profession = profession
        self.action_points = action_points
        self.move_speed = move_speed

    def complete_daily_task(self, daily_task_factors):
        zero_pl = False
        while not zero_pl:
            for i, task_factor in enumerate(daily_task_factors):
                self.do_task_by_profession(task_factor, i+1)
            pyautogui.moveTo(1558, 1149)
            zero_pl = testX.find_image_method()
            time.sleep(5)

    def do_task_by_profession(self, distance, task_id):
        # Step 1: Adjust character position
        time.sleep(1)
        print("{}开始在房间{}调整位置".format(self.name, task_id))
        hold_duration = distance / (self.move_speed * 1.4904)
        if distance > 0:
            keyboard.press('clear')
            time.sleep(hold_duration)
            keyboard.release('clear')
        elif distance < 0:
            keyboard.press('down')
            time.sleep(-hold_duration)
            keyboard.release('down')
        time.sleep(0.1)

        # Step 2: Read the JSON file and perform key simulations
        print("{}开始在房间{}输出".format(self.name, task_id))
        with open(f"keyboard_events_{self.name}_{self.profession}_{task_id}.json", "r") as json_file:
            key_events = json.load(json_file)

        for i, key_event in enumerate(key_events):
            event_type = key_event["event_type"]
            name = key_event["name"]

            if event_type == "down":
                keyboard.press(name)
            elif event_type == "up":
                keyboard.release(name)

            if i < len(key_events) - 1:
                time_interval = key_events[i + 1]["time"] - key_event["time"]
                if time_interval < 0:
                    print(key_event["time"])
                time.sleep(time_interval)

def switch_character():
    # 在这里实现您的切换角色逻辑
    CommonTool.switch_character(1082, 1014)
    pass

characters = [
    # Character('naiba', 'naibaNew', 2, 195),
    # Character('jianzhong', 'jianzhongNew', 2, 172),
    # Character('huahua', 'huahuaNew', 2, 278),
    # Character('rengying', 'rengyingNew', 2, 268),
    # Character('nvman', 'nvmanNew', 2, 203),
    # Character('jianhun1', 'jianhun1New', 2, 165),
    # Character('honggou', 'honggouNew', 2, 197),
    # Character('jianmo', 'jianmoNew', 2, 181),
    Character('xiuluo', 'xiuluoNew', 2, 154.5),
    Character('yingwu', 'yingwuNew', 2, 178),
    Character('wunv', 'wunvNew', 2, 159.5),
    # 更多角色...xxhA
]
daily_task_factors = [0, 17, -15, 25, 38, -152]  # 示例，您可以根据实际d情况设置[0, 0, 0.2, 0.1, 0.14, 0]
# CommonTool.moveto_en_san()
for i, character in enumerate(characters):
    print(f"当前角色：{character.name}, 职业：{character.profession}, 行动点数：{character.action_points}, 移动速度：{character.move_speed}")
    character.complete_daily_task(daily_task_factors)
    if i != len(characters) - 1:
        switch_character()
print("搬砖完成！")
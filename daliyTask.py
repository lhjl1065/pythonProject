import json
import keyboard
import time

import CommonTool


class Character:
    def __init__(self, name, profession, action_points, move_speed):
        self.name = name
        self.profession = profession
        self.action_points = action_points
        self.move_speed = move_speed

    def complete_daily_task(self, daily_task_factors):
        while self.action_points > 0:
            for i, task_factor in enumerate(daily_task_factors):
                self.do_task_by_profession(task_factor, i+1)
            self.action_points -= 6
            time.sleep(5)

    def do_task_by_profession(self, task_factor, task_id):
        # Step 1: Adjust character position
        time.sleep(1)
        print("{}开始在房间{}调整位置".format(self.name, task_id))
        hold_duration = task_factor * (177 / self.move_speed)
        if task_factor > 0:
            keyboard.press('clear')
            time.sleep(hold_duration)
            keyboard.release('clear')
        elif task_factor < 0:
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
                time.sleep(time_interval)

def switch_character():
    # 在这里实现您的切换角色逻辑
    CommonTool.switch_character(1080, 1138)
    pass

characters = [
    # Character('qigong', 'qigong', 164, 177),
    # Character('jianhun', 'jianhun', 188, 208),
    # Character('manyou', 'manyou', 68, 261),
    # Character('qiangpao', 'qiangpao', 121, 166),
    # Character('hongyan', 'hongyan', 188, 286),
    # Character('siling', 'siling', 92, 165.5),
    Character('naima', 'naima', 144, 166),
]
# time.sleep(60*33)
daily_task_factors = [0, -0.05, 0.1, 0.1, -0.05, -0.2]  # 示例，您可以根据实际情况设置[0, 0,XXX 0.2, 0.1, 0.14, 0]

for i, character in enumerate(characters):
    print(f"当前角色：{character.name}, 职业：{character.profession}, 行动点数：{character.action_points}, 移动速度：{character.move_speed}")
    character.complete_daily_task(daily_task_factors)
    if i != len(characters) - 1:
        switch_character()
print("搬砖完成！")
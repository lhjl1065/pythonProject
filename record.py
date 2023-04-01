import sys
import keyboard
import time
import json


def record_keyboard_input(file_name, duration):
    key_states = {}
    keyboard_events = []

    def on_key_event(event):
        key_state = keyboard.is_pressed(event.name)
        if key_states.get(event.name) != key_state:
            key_states[event.name] = key_state
            event_dict = {
                'event_type': event.event_type,
                'name': event.name,
                'time': event.time
            }
            keyboard_events.append(event_dict)

    keyboard.hook(on_key_event)

    print(f"开始记录键盘输入，请在 {duration} 秒内操作...")
    time.sleep(duration)

    keyboard.unhook_all()

    with open(file_name, 'w') as f:
        json.dump(keyboard_events, f)
    print("记录完毕")


def replay_keyboard_input(file_name):
    print("2秒后开始复现输入")
    time.sleep(2)
    with open(file_name, 'r') as f:
        json_data = json.load(f)

    prev_time = 0
    for event in json_data:
        if prev_time != 0:
            sleep_time = event['time'] - prev_time
            if sleep_time > 0:
                time.sleep(sleep_time)

        if event['event_type'] == keyboard.KEY_DOWN:
            keyboard.press(event['name'])
        elif event['event_type'] == keyboard.KEY_UP:
            keyboard.release(event['name'])
        prev_time = event['time']


def generate_file_name(a, b):
    return f"keyboard_events_{a}_{a}_{b}.json"


is_write = input("请输入是否监控 (true/false)：")
name = input("请输入角色名：")
number = input("请输入房间号：")
file_name = generate_file_name(name, number)
duration = 0
bool_value = is_write.lower() == "true"
if bool_value:
    duration = input("请输入时间（秒）：")
    print("开始记录键盘输入{}秒到文件{}".format(duration, file_name))
    record_keyboard_input(file_name, int(duration))
else:
    print("开始只读{}，复现键盘输入".format(file_name))
    replay_keyboard_input(file_name)

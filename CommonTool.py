import pyautogui
import time
import random
import pyautogui as pg
import keyboard
import json

def bezier_curve(t, p0, p1, p2):
    return (
        (1 - t) ** 2 * p0 + 2 * t * (1 - t) * p1 + t ** 2 * p2
    )

def smooth_move_to(x, y, duration=1, steps=100):
    start_x, start_y = pyautogui.position()
    control_x = random.randint(min(start_x, x), max(start_x, x))
    control_y = random.randint(min(start_y, y), max(start_y, y))

    for t in range(steps):
        t_normalized = t / steps
        new_x = bezier_curve(t_normalized, start_x, control_x, x)
        new_y = bezier_curve(t_normalized, start_y, control_y, y)
        pyautogui.moveTo(new_x, new_y, duration=0)
        time.sleep(duration / steps)

def choose_and_clik(x, y):
    time.sleep(3)  # 等待3秒，给用户一些准备时间
    smooth_move_to(x, y, duration=1)
    time.sleep(3)
    pg.dragTo(x, y, duration=0.5, button='left')


def moveto_nuo_si_pi_si():
    time.sleep(1)
    # 传送按钮 (808, 1234)
    choose_and_clik(809, 1239)
    time.sleep(1)

    # 点开地图 (1125, 732)
    choose_and_clik(1120, 731)
    time.sleep(1)

    # 选择地图 (868, 155)
    choose_and_clik(858, 162)
    time.sleep(1)

    # 天界 (809, 233)
    choose_and_clik(804, 236)
    time.sleep(1)

    #    诺斯匹斯 (1093, 288)
    choose_and_clik(1104, 291)
    time.sleep(1)

    # 地下城入口 (941, 725)
    choose_and_clik(938, 756)
    time.sleep(1)

    # 确认传送(1114, 732)
    choose_and_clik(1123, 734)
    time.sleep(1)


def moveto_en_san():
    print("移动角色进入恩山英噩级")
    simulate_keyboard_input_from_json('keyboard_events_moveto_en_san.json')


def simulate_keyboard_input_from_json(json_file):
    print("开始根据{}复现键盘输入...".format(json_file))
    time.sleep(1)
    # 从json文件读取键盘事件，并模拟键盘输入操作
    json_data = []
    with open(json_file, 'r') as f:
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
    time.sleep(5)

    print("键盘输入复现完成！")


def switch_character(x, y):
    time.sleep(10)
    keyboard.press('f12')
    time.sleep(0.1)
    keyboard.release('f12')
    time.sleep(10)
    keyboard.press('esc')
    time.sleep(0.1)
    keyboard.release('esc')
    time.sleep(1)
    choose_and_clik(x, y)
    time.sleep(3)
    keyboard.press('page down')
    time.sleep(0.1)
    keyboard.release('page down')
    time.sleep(2)
    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')
    # 移动到诺斯匹斯
    moveto_nuo_si_pi_si()
    # 进入恩山英噩级
    moveto_en_san()

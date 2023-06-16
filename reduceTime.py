import json

def adjust_key_press_time(json_file, new_json_file):
    # 读取 JSON 文件
    with open(json_file, 'r') as f:
        data = json.load(f)

    # 创建一个新的列表来存储调整后的数据
    adjusted_data = []

    # 用字典记录每个键的按下时间
    key_press_times = {}

    # 遍历每个元素进行处理
    for i in range(len(data)):
        event_type = data[i]['event_type']
        key_name = data[i]['name']
        event_time = data[i]['time']

        if event_type == 'down':
            key_press_times[key_name] = event_time
            # 直接将按下动作添加到调整后的数据列表中
            adjusted_element = {
                'event_type': event_type,
                'name': key_name,
                'time': event_time
            }
            adjusted_data.append(adjusted_element)
        elif event_type == 'up' and key_name in key_press_times:
            down_time = key_press_times[key_name]
            time_diff = event_time - down_time
            adjusted_time = down_time + (time_diff / 106 * 100)

            # 创建调整后的元素
            adjusted_element = {
                'event_type': event_type,
                'name': key_name,
                'time': adjusted_time
            }

            # 添加到调整后的数据列表
            adjusted_data.append(adjusted_element)

            # 从键按下时间字典中移除该键
            del key_press_times[key_name]

    # 将剩余的按下动作处理为未松开状态
    for key_name, down_time in key_press_times.items():
        adjusted_element = {
            'event_type': 'down',
            'name': key_name,
            'time': down_time
        }
        adjusted_data.append(adjusted_element)

    adjusted_data.sort(key=lambda x: x['time'])

    # 将调整后的数据写入新的 JSON 文件
    with open(new_json_file, 'w') as f:
        json.dump(adjusted_data, f, indent=2)

    print('Adjusted JSON file created: adjusted.json')

# 调用函数并传入 JSON 文件路径
adjust_key_press_time(r'C:\Users\Administrator\PycharmProjects\pythonDNF\keyboard_events_wunv_wunv_6.json', 'keyboard_events_wunv_wunvNew_6.json')

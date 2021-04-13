# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         SendMsg
# Description:  这里写的是一些无关于数据库的消息判断与对消息的反应
# Author:       M4XLMUM
# Date:         2021/4/12
# -------------------------------------------------------------------------------
import random
import requests


url = 'http://127.0.0.1:5700'
def send(all_message, message):
    if all_message['message_type'] == 'group' and message != 'null':
        group_id = all_message['group_id']
        text = {
            'group_id': group_id,
            'message': message
        }
        response = requests.post(url=url + "/send_group_msg", data=text)
        print(response.json())

    if all_message['message_type'] == 'private' and message != 'null':
        user_id = all_message['user_id']
        text = {
            'user_id': user_id,
            'message': message
        }
        response = requests.post(url=url + "/send_private_msg", data=text)
        print(response.json())


# 信息处理之菜单，涩图
def common_msg(all_message, admin):
    message = 'null'
    if all_message['message'] == '菜单':
        message = "            菜单:\n1.涩图          2.一言\n3.经典语录      4.舔狗日记\n5.历史上的今天(尚未完成)"
    if '儿子' in all_message['message'] and not admin:
        message = "就你，你就是一坨屎"
    if all_message['message'] == '涩图':
        rd = random.randint(0, 81)
        message = "[CQ:image,file=1.jpg,url=file:/home/qqbot/plugin/realsetu/picture{0}.jpg,type=show,id=40000]".format(rd)
    send(all_message, message)
# 信息处理之菜单，涩图结束


# 信息处理之api信息处理
def api_msg(all_message):
    # 非json消息处理
    apitext = 'null'
    if all_message['message'] == '舔狗日记':
        api = 'https://api.oick.cn/dog/api.php'
        apitext = requests.get(api).text
    if all_message['message'] == '经典语录':
        api = 'https://api.oick.cn/yulu/api.php'
        apitext = requests.get(api).text
    if all_message['message'] == '一言':
        api = 'https://api.oick.cn/yiyan/api.php'
        apitext = requests.get(api).text
    '''
        # json消息处理
        if all_message['message'] == '历史上的今天':
            api = 'https://api.muxiaoguo.cn/api/lishijr'
            apitext = requests.get(api).json()
            message = "[CQ:json,data={0}]".format(str(apitext['data']).replace("&", '&amp;').replace(",", '&#44;').replace("[", '&#91').replace("]", '&#93;'))
    '''
    message = apitext[1:len(apitext) - 1]
    if message != 'ul':
        send(all_message, message)
# 信息处理之api信息处理结束
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         talk
# Description:  bot与群友交流
# Author:       M4XLMUM
# Date:         2021/4/12
# -------------------------------------------------------------------------------
import json
import SendMsg

with open("./words.json", "r", encoding="utf-8") as file:
    words = file.read()
words = json.loads(words)


# 关键词识别
def talk_msg(all_message):
    key = all_message['message']
    if key in words:
        message = words['{0}'.format(key)]
        SendMsg.send(all_message, message)


# 教机器人学习
def teach_msg(all_message, admin):
    keywords = ['菜单', '涩图', '一言', '经典语录', '舔狗日记', '历史上的今天', 'delete', 'teach', '儿子', '爸爸']

    usermsg = all_message['message']
    tempflag = 1
    # 添加字典元素
    if usermsg[:5] == 'teach':
        text = usermsg[6:].split(' ')
        # 关键词判断
        for i in keywords:
            if i in text:
                tempflag = 0
                break

        key = text[0]
        value = text[1]
        if key not in words and tempflag:
            words["{0}".format(key)] = value
            SendMsg.send(all_message, "添加成功")
        else:
            SendMsg.send(all_message, "黑客吃狗屎")
    # 删除字典元素
    if usermsg[:6] == 'delete':
        if not admin:
            SendMsg.send(all_message, "你没有权限删除信息")
            return
        key = usermsg[7:]
        if key in words:
            try:
                del words['{0}'.format(key)]
            except:
                SendMsg.send(all_message, "查无此项")
            else:
                SendMsg.send(all_message, "删除成功")
        else:
            SendMsg.send(all_message, "查无此项")
    save_words()


def save_words():
    content = json.dumps(words, ensure_ascii=False)
    with open("./words.json", "w", encoding="utf-8") as file:
        file.write(content)

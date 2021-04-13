# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         connect
# Description:  主要逻辑
# Author:       M4XLMUM
# Date:         2021/4/12
# -------------------------------------------------------------------------------
import SendMsg
import connect
import talk

# 主循环事件处理
while 1:
    all_message = connect.rev_msg()
    if all_message is None:
        continue

    # 管理员权限
    admin = 0
    admingroup = [2994016494]   # 在这里添加管理员组
    for i in admingroup:
        if all_message['sender']['user_id'] == i:
            admin = 1
    # 关键词触发信息处理
    try:
        talk.teach_msg(all_message, admin)
        talk.talk_msg(all_message)
        SendMsg.common_msg(all_message, admin)  # 一般信息处理
        SendMsg.api_msg(all_message)     # api信息处理
    except KeyError as e:
        print(e)
        continue
    # 关键词部分结束

# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         connect
# Description:  连接和判断
# Author:       M4XLMUM
# Date:         2021/4/12
# -------------------------------------------------------------------------------
import socket
import json


ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.bind(('127.0.0.1', 5701))
ListenSocket.listen(100)

HttpResponseHeader = ('HTTP/1.1 200 OK'
                      'Content-Type: text/html')


# 定位有效信息
def request_to_json(msg):
    index = msg.find('{')
    if msg[index] == "{" and msg[len(msg) - 2] == "}" and msg[index:index + 12] != "{\"interval\":":
        tempmsg = msg[index:len(msg) - 1]
        print(tempmsg)
        return json.loads(tempmsg)
    return None


# 需要循环执行，返回值为json格式
def rev_msg():  # json or None
    conn, Address = ListenSocket.accept()
    Request = conn.recv(1024).decode(encoding='utf-8')
    rev_json = request_to_json(Request)
    conn.sendall(HttpResponseHeader.encode(encoding='utf-8'))  # 200OK事件响应
    conn.close()
    return rev_json
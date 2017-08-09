# coding=utf-8
# pip install douyu
# import socket
#
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('openbarrage.douyutv.com',8601))
# s.send('type@=loginreq/roomid@=2046501/')
# print s.recv(1024)
from douyu.chat.room import ChatRoom
import time
import keyboard

i = 0


def on_chat_msg(msg):
    global i
    i = i + 1
    print '[' + str(i) + ']' + time.strftime("%I:%M:%S", time.localtime()) + '[%s]:%s' % (msg.attr('nn'), msg.attr('txt'))
    txt = msg.attr('txt')
    if txt == 'u':
        keyboard.press_and_release('up')
    elif txt == 'd':
        keyboard.press_and_release('down')
    elif txt == 'l':
        keyboard.press_and_release('left')
    elif txt == 'r':
        keyboard.press_and_release('right')
    else:
        keyboard.press_and_release('esc')


room = ChatRoom('642949')
room.on('chatmsg', on_chat_msg)
room.knock()

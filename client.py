#!/usr/bin/env python
import socket
import sys
import utility
import threading
import common
import dslibrary as dl

message_queue = dl.Queue()

def msg_dispatcher(socket):
    while True:
        if not message_queue.isEmpty():
            message = message_queue.pop() 
            utility.send_message(socket, message)

def parse_text(text):
    tokens = text.split(':')
    recipient_list = tokens[0]
    msg = tokens[1]
    recipients = recipient_list.split(',')
    return (recipients, msg)
        
def input_listener(socket, myname):
    while True:
        text = raw_input()
        recipients, text = parse_text(text)
        new_message = utility.message(text, myname, recipients)
        message_queue.push(new_message)

def server_listner(socket):
    while True:
        message = utility.recieve_message(socket)
        print "{}==>{}".format(message.sender, message.get_text())

def main(server, port):
    print "Enter your name"
    myname = raw_input()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    msg = utility.message(myname, myname, ['server'])
    utility.send_message(s, msg)
    thread1 = threading.Thread(target=input_listener, args=[s, myname])
    thread2 = threading.Thread(target=server_listner, args=[s])
    thread3 = threading.Thread(target=msg_dispatcher, args=[s])
    thread1.start()
    thread2.start()
    thread3.start()

main(sys.argv[1], int(sys.argv[2]))


#!/usr/bin/env python
import socket
import sys
import utility
import threading
import common


class message(object):

    def  __init__(self, text):
        self.text = text
        self.id = common.generate_next_msg_id()

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id
        
class sent_message(message):

    def __init__(self, text, recipients, sender):
        message.__init__(self, text)
        self.set_sent_time()
        self.set_delivered_time()
        self.recipients = recipients
        self.sender = sender 

    def set_sent_time(self):
        self.sent_time = common.get_current_time()

    def set_delivered_time(self, time=None):
        self.delivered_time = time

    def get_sent_time(self):
        return self.sent_time

    def get_delivered_time(self):
        return self.delivered_time

class received_message(message):
    
    def __init__(self, text):
        message.__init__(self, text)
        self.set_received_time(common.get_current_time())

    def set_received_time(self, time):
        self.received_time = time

    def get_received_time(self):
        return self.received_time


def input_listener(socket):
    while True:
        text = raw_input()
        utility.send_message(socket,text)

def server_listner(socket):
    while True:
        new_message = received_message(utility.recieve_message(socket))
        print new_message.get_text()

def main(server, port):
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect((server, port))
    thread1 = threading.Thread(target=input_listener, args=[s])
    thread2 = threading.Thread(target=server_listner, args=[s])
    thread1.start()
    thread2.start()

main(sys.argv[1], int(sys.argv[2]))


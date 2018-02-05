#!/usr/bin/env python
import socket
import sys
import utility
import threading
import common


def parse_text(text):
    tokens = text.split(':')
    return (tokens[0], tokens[1])
        
def input_listener(socket):
    while True:
        text = raw_input()
        recipients, text = parse_text(text)
        new_message = utility.message(text, 'hitesh', ['kumar'])
        utility.send_message(socket, new_message)

def server_listner(socket):
    while True:
        message = utility.recieve_message(socket)
        print "{}==>{}".format(message.sender, message.get_text())

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


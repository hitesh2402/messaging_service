#!/usr/bin/env python
import socket
import threading
import common
import utility as u
import dslibrary as dl


message_queue = dl.Queue()
pending_messages = {}
users = {}

def msg_dispatcher():
    while True:
        if not message_queue.isEmpty():
            message = message_queue.pop()
            print "one message dispatched"
            for recipient in message.recipients:
                if recipient in users:
                    users[recipient].send_message(message)
                else:
                    if recipient not in pending_messages:
                        pending_messages[recipient] = dl.Queue()
                    pending_messages[recipient].push(message)

class Client():
    def __init__(self, name, socket):
        self.name = name
        self.socket = socket
        if self.name in pending_messages:
            self.deliver_unsend_messages()

    def deliver_unsend_messages(self):
        q = pending_messages[self.name]
        while not q.isEmpty():
            message = q.pop()
            u.send_message(self.socket, message)

    def send_message(self, message):
        u.send_message(self.socket, message)

def register_client(clientsocket):
    msg = u.recieve_message(clientsocket)
    nickname = msg.get_text()
    client = Client(nickname, clientsocket)
    users[nickname] = client
    print "%s joined the chatroom" % (nickname)
    client_listener = threading.Thread(target=start_listening_to_client, args=[client])
    client_listener.start()

def enque_message(message):
    print "new message added to the queue"
    message_queue.push(message)

def start_listening_to_client(client):
    socket = client.socket
    while True:
        msg = u.recieve_message(socket)
        msgtext = "{}:{}".format(msg.sender, msg.get_text())
        print msgtext
        enque_message(msg)


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 9988))
serversocket.listen(5)
client_threads = []
postman = threading.Thread(target=msg_dispatcher, args=[])
postman.start()
while True:
    (clientsocket, address) = serversocket.accept()
    register_client(clientsocket)

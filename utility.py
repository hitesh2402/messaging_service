#!/usr/bin/env python

import struct
import json
import common

class message(object):

    def  __init__(self, text='None', sender='None', recipients='None'):
        self.text = text
        self.id = common.generate_next_msg_id()
        self.set_sent_time()
        self.set_delivered_time()
        self.recipients = recipients
        self.sender = sender 

    def set_sent_time(self):
        self.sent_time = common.get_current_time()

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id

    def set_delivered_time(self, time='None'):
        self.delivered_time = time

    def get_sent_time(self):
        return self.sent_time

    def get_delivered_time(self):
        return self.delivered_time

def recvall(sock, size):
    data = ''
    while len(data) < size:
        dataTmp = sock.recv(size-len(data))
        data += dataTmp
        if dataTmp == '':
            raise RuntimeError("socket connection broken")
    return data

def recvall2(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def serialize(data):
    jsonstring = json.dumps(data.__dict__)
    return jsonstring

def deserialize(data):
    data_dict = json.loads(data)
    msg = message()
    msg.__dict__ = data_dict
    return msg


def send_message(sock, msg):
    data = serialize(msg)
    length = len(data)

    frmt = "=%ds" % length
    packedMsg = struct.pack(frmt, data)
    packedHdr = struct.pack('=I', length)

    sock.sendall(packedHdr)
    sock.sendall(packedMsg)

def recieve_message(sock):
    lengthbuf = recvall(sock, 4)
    s = struct.unpack('=I', lengthbuf)
    length = s[0]
    data = recvall(sock, length)
    frmt = "=%ds" % length
    encoded = struct.unpack(frmt, data)
    msgpacket = deserialize(encoded[0])
    return msgpacket



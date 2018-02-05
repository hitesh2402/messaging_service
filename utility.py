#!/usr/bin/env python

import struct
import json

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
    return json.dumps(data)


def send_message(sock, msgpacket):
    data = serialize(msgpacket)
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
    msg = struct.unpack(frmt, data)
    msgpacket = json.loads(msg[0])
    return msgpacket



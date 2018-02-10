#!/usr/bin/env python

class Queue(object):

    class Node(object):
        def  __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def push(self, item):
        new_node = Queue.Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.head is None:
            raise Exception("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        return data

    def size(self):
        return len(self.data)

if __name__ == '__main__':
    main()


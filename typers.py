def find_id(ids: int):
    import ctypes
    
    return ctypes.cast(ids, ctypes.py_object).value


class zhan():
    def __init__(self, what: list | str | set | tuple = []):
        self.what = list(what)
    
    def out(self):
        x = self.what[-1]
        self.what.pop()
        return x
    
    def z_in(self, what):
        self.what.append(what)
    
    def lock(self):
        return self.what


class lei():
    def __init__(self, what: list | str | set | tuple = []):
        self.what = list(what)
    
    def out(self):
        x = self.what[0]
        self.what.pop(0)
        return x
    
    def z_in(self, what):
        self.what.append(what)
    
    def lock(self):
        return self.what


class Node:
    def __init__(self, data=None, val=None, next=None):
        self.data = data
        self.val = val
        self.next = next


# 双链表类
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
    
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.prepend(data)
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("Position out of range")
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node

    def remove(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        Node_list = []
        while current is not None:
            Node_list.append(current.data)
            current = current.next
        return Node_list


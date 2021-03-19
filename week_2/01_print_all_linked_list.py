
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)


    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.append(9)
linked_list.print_all()

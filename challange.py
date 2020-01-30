class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLlist:
    def __init__(self, node=None):
        self.head = node

    def add_to_head(self, value):
        new_node = SLNode(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

def find_mid_node(list):
    counter = 0
    middle = list.head
    current = list.head

    while current.nex:
        counter +=1
        current = current.next
        if counter % 2 is 0:
            middle = middle.next
        return middle


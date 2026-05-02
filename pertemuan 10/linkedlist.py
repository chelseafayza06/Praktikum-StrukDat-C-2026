# bagian 2 pakai linkedlist 
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 #utk lacak ukuran

    def is_empty(self):
        return self.top is None

    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url

    def peek(self):
        if self.is_empty():
            return None
        return self.top.url

    def size(self):
        return self.count
    
myStack = StackLinkedList()

myStack.push('https:chelsea//.id')
myStack.push('https:sande//.id')
myStack.push('https:fira//.id')

# print("LinkedList: ", end="")
# #myStack.traverseAndPrint()
# print("Peek: ", myStack.peek())
# print("Pop: ", myStack.pop())
# print("LinkedList after Pop: ", end="")
# #myStack.traverseAndPrint()
# print("isEmpty: ", myStack.is_empty())
# print("Size: ", myStack.size())


class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):  
            print("enqueue None")
            return
        else:
            if self.head == -1:
                self.head = 0
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
        print(f"enqueue <{data}>")

    # Delete an element from the circular queue
    def dequeue(self):
        if self.head == -1:
            print("dequeue None")
            return
        else:
            element = self.queue[self.head]
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.k
        print(f"dequeue <{element}>")
        return element

    def peek(self):
        if self.head == -1:
            print("peek None")
            return
        else:
            element = self.queue[self.head]
            print(f"peek <{element}>")
            return element

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedListQueue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        print(f"enqueue <{data}>")

    def dequeue(self):
        if self.head is None:
            print("dequeue None")
            return
        else:
            data = self.head.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            print(f"dequeue <{data}>")
            return data

    def peek(self):
        if self.head is None:
            print("peek None")
            return
        else:
            data = self.head.data
            print(f"peek <{data}>")
            return data
        
if __name__ == "__main__":
    # Create a queue with a fixed size
    queue = CircularQueue(5)

    # Test regular operations
    queue.enqueue(1)  
    queue.enqueue(2)  
    queue.peek()  
    queue.dequeue()  
    queue.enqueue(3)  
    queue.enqueue(4)  
    queue.enqueue(5)  
    queue.enqueue(6)  
    queue.peek()  
    queue.dequeue()  
    queue.enqueue(7)  
    queue.enqueue(8)  
    queue.peek()  
    queue.dequeue()  
    queue.enqueue(9)  
    queue.enqueue(10)  

    # Test corner cases
    queue.enqueue(11)  # Should print "enqueue None" (queue is full)
    queue.dequeue()  
    queue.dequeue()  
    queue.dequeue()  
    queue.dequeue()  
    queue.dequeue()  
    queue.dequeue()  # Should print "dequeue None" (queue is empty)
    queue.peek()  # Should print "peek None" (queue is empty)

    # Test operations after corner cases
    queue.enqueue(12)  
    queue.enqueue(13)  
    queue.peek()  
    queue.dequeue()  
    queue.enqueue(14)  
    queue.enqueue(15)  
    queue.enqueue(16)  
    queue.enqueue(17)  
    queue.peek()  
    queue.dequeue()  
    queue.enqueue(18)  
    queue.enqueue(19)  
    queue.peek()  
    queue.dequeue()  
    queue.enqueue(20)  
    queue.enqueue(21)  

    # Test the CircularLinkedListQueue in the same way
    linked_list_queue = CircularLinkedListQueue()
    
    # Test regular operations
    linked_list_queue.enqueue(1)  
    linked_list_queue.enqueue(2)  
    linked_list_queue.peek()  
    linked_list_queue.dequeue()  
    linked_list_queue.enqueue(3)  
    linked_list_queue.enqueue(4)  
    linked_list_queue.enqueue(5)  
    linked_list_queue.enqueue(6)  
    linked_list_queue.peek()  
    linked_list_queue.dequeue()  
    linked_list_queue.enqueue(7)  
    linked_list_queue.enqueue(8)  
    linked_list_queue.peek()  
    linked_list_queue.dequeue()  
    linked_list_queue.enqueue(9)  
    linked_list_queue.enqueue(10)  

    # Test corner cases
    linked_list_queue.dequeue()  
    linked_list_queue.dequeue()  
    linked_list_queue.dequeue()  
    linked_list_queue.dequeue()  
    linked_list_queue.dequeue()  
    linked_list_queue.dequeue()  # Should print "dequeue None" (queue is empty)
    linked_list_queue.peek()  # Should print "peek None" (queue is empty)

    # Test operations after corner cases
    linked_list_queue.enqueue(12)  
    linked_list_queue.enqueue(13)  
    linked_list_queue.peek()  
    linked_list_queue.dequeue()  
    linked_list_queue.enqueue(14)  
    linked_list_queue.enqueue(15)  
    linked_list_queue.enqueue(16)  
    linked_list_queue.enqueue(17)  
    linked_list_queue.peek()  
    linked_list_queue.dequeue()  
    linked_list_queue.enqueue(18)  
    linked_list_queue.enqueue(19)  
    linked_list_queue.peek()  
    linked_list_queue.dequeue()  
    linked_list_queue.enqueue(20)  
    linked_list_queue.enqueue(21)  
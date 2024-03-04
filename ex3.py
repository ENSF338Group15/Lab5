# 5. From the histogram it is clear that the ArrayStack has a greater frquency and shifted towards
# less time, therefore it has shorter execution times and thus performed better than the LinkedListStack.
# This is because in a array stack, the time complexity of the push and pop operations are O(1) while 
# the time complexity for push and pop operations for a linked list stack are O(n) as we need to traverse 
# though the entire list after each operation.

import random
import timeit
import matplotlib.pyplot as plt

class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.empty():
            return None
        else:
            return self.stack.pop()
    
    def empty(self):
        return len(self.stack) == 0
    
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        return removed.data

def generate_tasks(n=10000):
    tasks = []
    for _ in range(n):
        task_type = 'push' if random.random() < 0.7 else 'pop'
        tasks.append(task_type)
    return tasks

def execute_tasks(queue, tasks):
    for task in tasks:
        if task == 'push':
            queue.push(1)
        else:
            queue.pop()

def measure_performance(queue_class, tasks_lists):
    times = []
    for tasks in tasks_lists:
        queue = queue_class()
        start_time = timeit.default_timer()
        execute_tasks(queue, tasks)
        end_time = timeit.default_timer()
        times.append(end_time - start_time)
    return times

tasks_lists = [generate_tasks() for _ in range(100)]

array_stack_times = measure_performance(ArrayStack, tasks_lists)
linked_list_stack_times = measure_performance(LinkedListStack, tasks_lists)

print('PriorityQueueSort average time:', sum(array_stack_times) / len(array_stack_times))
print('PriorityQueueInsertion average time:', sum(linked_list_stack_times) / len(linked_list_stack_times))

plt.hist(array_stack_times, bins=50, alpha=0.7, label='ArrayStack', density=True)
plt.hist(linked_list_stack_times, bins=50, alpha=0.7, label='LinkedListStack', density=True)
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Performance of Stack Implementations')
plt.show()
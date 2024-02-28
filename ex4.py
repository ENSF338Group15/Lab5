import random
import timeit
import matplotlib.pyplot as plt

# Queue using Python arrays
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop()

# Node class for singly-linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Queue using a singly-linked list
class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next, self.tail = new_node, new_node
        else:
            self.head = self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed.data

# Function to generate random tasks
def generate_tasks(n=10000):
    tasks = []
    for _ in range(n):
        task_type = 'enqueue' if random.random() < 0.7 else 'dequeue'
        tasks.append(task_type)
    return tasks

# Function to execute tasks on a given queue
def execute_tasks(queue, tasks):
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(1)
        else:
            queue.dequeue()

# Function to measure performance
def measure_performance(queue_class, tasks_lists):
    times = []
    for tasks in tasks_lists:
        start_time = timeit.default_timer()
        execute_tasks(queue_class(), tasks)
        end_time = timeit.default_timer()
        times.append(end_time - start_time)
    return times

# Generate 100 lists of tasks
tasks_lists = [generate_tasks() for _ in range(100)]

# Measure performance for both queue implementations
array_queue_times = measure_performance(ArrayQueue, tasks_lists)
linked_list_queue_times = measure_performance(LinkedListQueue, tasks_lists)

# Print results
print('ArrayQueue average time:', sum(array_queue_times) / len(array_queue_times))
print('LinkedListQueue average time:', sum(linked_list_queue_times) / len(linked_list_queue_times))

# Plot distributions
plt.hist(array_queue_times, bins=20, alpha=0.5, label='ArrayQueue')
plt.hist(linked_list_queue_times, bins=20, alpha=0.5, label='LinkedListQueue')
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Performance of Queue Implementations')
plt.show()

# Discussion of results (question 5):
# From the histogram it is clear that the LinkedListQueue has a greater frquency and shifted towards
# less time, therefore it has shorter execution times and thus performed better than the ArrayQueue in 
# this scenario. This is because in a singly-linked list, the enqueue and dequeue operations are O(1)
# compared to that of an ArrayQueue which has a complxity of O(n) when adding a new element at the head.

# 5. From our performance measurements results, we can conlude that PriorityQueueInsertion is faster than
# PriorityQueueSort. This is because insertion for each new element after finding its position is generally
# faster than sorting entire the array with mergesort after every enqueue operation in PriorityQueueSort.

import timeit
import random

class PriorityQueueSort:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        self.merge_sort(0, len(self.queue) - 1)

    def dequeue(self):
        if self.empty():
            return None
        else:
            return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0

    def merge_sort(self, start, end):
        if start < end:
            mid = (start + end) // 2
            self.merge_sort(start, mid)
            self.merge_sort(mid + 1, end)
            self.merge(start, mid, end)

    def merge(self, start, mid, end):
        left_half = self.queue[start:mid + 1]
        right_half = self.queue[mid + 1:end + 1]

        i = j = 0
        k = start

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                self.queue[k] = left_half[i]
                i += 1
            else:
                self.queue[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            self.queue[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            self.queue[k] = right_half[j]
            j += 1
            k += 1

class PriorityQueueInsertion:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if len(self.queue) == 0:
            self.queue.append(item)
        else:
            index = 0
            while index < len(self.queue) and self.queue[index] <= item:
                index += 1
            self.queue.insert(index, item)

    def dequeue(self):
        if self.empty():
            return None
        else:
            return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0
    
def generate_tasks(n=1000):
    tasks = []
    for _ in range(n):
        task_type = 'enqueue' if random.random() < 0.7 else 'dequeue'
        tasks.append(task_type)
    return tasks

def execute_tasks(queue, tasks):
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(1)
        else:
            queue.dequeue()

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

queue_sort_times = measure_performance(PriorityQueueSort, tasks_lists)
insertion_sort_times = measure_performance(PriorityQueueInsertion, tasks_lists)

print('PriorityQueueSort average time:', sum(queue_sort_times) / len(queue_sort_times))
print('PriorityQueueInsertion average time:', sum(insertion_sort_times) / len(insertion_sort_times))

# Used ChatGPT to generate PriorityQueueSort and PriorityQueueInsertion.
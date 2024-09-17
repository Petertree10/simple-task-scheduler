import argparse
import heapq
import sys


class Task:
    def __init__(self, name, description, priority) -> None:
        self.name = name
        self.description = description
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f"Task({self.priority}, {self.name})"
    
 
class TaskScheduler:
    def __init__(self) -> None:
        self.taskQueue = []
    
    def add_task(self):
        name = input('Task name: ')
        description = input('Task description: ')
        priority = input('Priority (1-10): ')
        heapq.heappush(self.taskQueue, Task(name, description, priority))
        print('Task added!\n')

    def remove_task(self, task):
        self.taskQueue.remove(task)

    def view_tasks(self):
        l = self.taskQueue
        l.sort()
        print('Tasks in priority order:')
        for i, task in enumerate(l):
            print(f'{i+1}. [Priority {task.priority}] {task.name}: {task.description}')
        print('\n')

    def complete_task(self):
        task = heapq.heappop(self.taskQueue)
        print(f'Next task completed: [Priority {task.priority}] {task.name}: {task.description}\n')

def prompt_user():
    print('1. Add a new task\n2. View tasks\n3. Complete the next task\n4. Exit\n')
    return input('Enter your choice: ')

if __name__ == "__main__":
    taskScheduler = TaskScheduler()
    while True:
        prompt = prompt_user()
        if prompt == '1':
            taskScheduler.add_task()
        elif prompt == '2':
            taskScheduler.view_tasks()
        elif prompt == '3':
            taskScheduler.complete_task()
        elif prompt == '4':
            print('Exiting the Task Scheduler. Goodbye!')
            sys.exit()
        else:
            print('Option invalid: Please try again.\n')



        





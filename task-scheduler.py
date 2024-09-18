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
        if name.strip() == "":
            print('Invalid input: Task name cannot be empty.\n')
            return
        description = input('Task description: ')
        if description.strip() == "":
            print('Invalid input: Task description cannot be empty.\n')
            return
        try:
            priority = int(input('Priority (1-10): '))
            if not 1 <= priority <= 10:
                raise ValueError
        except ValueError:
            print('Invalid input: Priority must be a number between 1 and 10.\n')
            return
        
        heapq.heappush(self.taskQueue, Task(name, description, priority))
        print('Task added!\n')

    def view_tasks(self):
        if len(self.taskQueue) == 0:
            print('No tasks available to view.\n')
            return
        sorted_tasks = sorted(self.taskQueue)
        print('Tasks in priority order:')
        for i, task in enumerate(sorted_tasks):
            print(f'{i+1}. [Priority {task.priority}] {task.name}: {task.description}')
        print('\n')

    def complete_task(self):
        if len(self.taskQueue) == 0:
            print('No tasks available to complete.\n')
            return
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



        





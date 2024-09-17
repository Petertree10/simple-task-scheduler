# Task Scheduler with Priority Queue in Python

## Project Overview

This project implements a **Task Scheduler** using Python, where tasks are managed and executed based on their **priority**. The scheduler uses a **min-heap** (priority queue) to ensure that tasks with higher priority are executed first (with smaller priority numbers being higher priority).

You can use this tool to:

- Add tasks with a specific priority, description, and name.
- View all tasks sorted by priority.
- Remove tasks as they are completed, always starting with the highest priority task.

---

## Features

1. **Add New Task**: Add a task with a name, description, and priority (1 = highest priority, 10 = lowest priority).
2. **View Tasks**: View all tasks, sorted in ascending order of priority.
3. **Complete Task**: Complete and remove the task with the highest priority.
4. **Error Handling**: The scheduler validates inputs (like ensuring task names and descriptions aren't empty, and that priority values are between 1 and 10).
5. **Efficient Priority Management**: The task scheduler uses Python’s built-in **heapq** module to efficiently manage the priority queue.

---

## Technologies Used

- **Python 3.x**
- **heapq module**: This module is used to manage the heap (priority queue) operations efficiently.

---

## How to Run the Project

### Requirements

- Python 3.x

### Steps to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Petertree10/simple-task-scheduler.git
   cd simple-task-scheduler
   ```

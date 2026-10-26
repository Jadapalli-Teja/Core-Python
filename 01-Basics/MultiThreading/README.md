
# Python Multithreading — Complete Beginner's Guide

This README explains Python multithreading from the basics, including processes, threads, main thread execution, internal execution flow, thread creation, `start()`, `run()`, `join()`, `sleep()`, daemon threads, race conditions, and locks.

---

# 1. How Does a Python Program Execute?

Before learning multithreading, we need to understand how a normal Python program runs.

Consider this program:

```python
print("A")
print("B")
print("C")
```

Output:

```text
A
B
C
```

### Step-by-step execution

1. We write the code in a Python file.
2. We run the file using Python.
3. Python starts executing the program.
4. The first `print()` displays `A`.
5. The second `print()` displays `B`.
6. The third `print()` displays `C`.
7. The program finishes.

In this example, the statements execute in order in the main thread.

## What is the main thread?

The **main thread** is the thread that begins executing the top-level code of a normal Python script.

A Python program already has a main thread. We do not need to create it manually.

Example:

```python
import threading

print("Statement 1")
print("Statement 2")
print("Current thread:", threading.current_thread().name)
```

Output:

```text
Statement 1
Statement 2
Current thread: MainThread
```

The name of the main thread is usually `MainThread`.

### Internal execution flow

```text
Run Python program
        |
        v
Python process starts
        |
        v
Main thread begins execution
        |
        v
Statement 1 executes
        |
        v
Statement 2 executes
        |
        v
Program continues
```

**Important:** Defining a function does not execute it. The function executes when it is called.

---

# 2. What Is a Process?

A **process** is a running instance of a program.

For example:
- Running a Python script creates a process.
- Opening a text editor runs a process.
- Opening a browser normally involves one or more processes.

A process has resources such as memory, program state, and operating-system resources.

A process can contain one or more threads.

# 3. What Is a Thread?

A **thread** is a sequence of instructions that can be scheduled for execution within a process.

Think of a process as a kitchen and threads as workers inside that kitchen.

- Process = kitchen
- Threads = workers
- Tasks = jobs to complete

A process can contain multiple threads that make progress concurrently.

## Process vs. Thread

| Process | Thread |
|---|---|
| A running instance of a program | An execution path within a process |
| Has its own process-level memory space | Threads in the same process share process memory |
| Usually more isolated from other processes | Can access shared objects in its process |
| Can contain multiple threads | Belongs to a process |

Threads share process memory, but each thread has its own execution state, including its own call stack.

---

# 4. What Is Multithreading?

**Multithreading** means using multiple threads within a single process so that multiple tasks can make progress concurrently.

### Real-life example

Imagine you are downloading a file while listening to music.

You do not want the music to stop every time the download waits for a response.

A program can use separate threads so that one task can make progress while another task is waiting.

### Where is multithreading useful?

- Downloading files
- Making network requests
- Reading and writing files
- Waiting for server responses
- Performing multiple I/O operations

### Does multithreading always make programs faster?

No.

Threads have overhead. In standard CPython, the Global Interpreter Lock (GIL) generally prevents multiple threads from executing Python bytecode simultaneously within one interpreter.

Multithreading is especially useful for **I/O-bound tasks**, where threads frequently wait for input or output.

---

# 5. Single-Threaded Execution

Consider this program:

```python
import time

def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 finished")

def task2():
    print("Task 2 started")
    time.sleep(2)
    print("Task 2 finished")

task1()
task2()

print("Program finished")
```

Output:

```text
Task 1 started
Task 1 finished
Task 2 started
Task 2 finished
Program finished
```

### Step-by-step execution

1. Python defines `task1()`.
2. Python defines `task2()`.
3. Python calls `task1()` in the main thread.
4. `Task 1 started` is printed.
5. `time.sleep(2)` pauses the main thread for approximately two seconds.
6. `Task 1 finished` is printed.
7. `task1()` returns.
8. Python calls `task2()`.
9. The main thread pauses for approximately two more seconds.
10. `Task 2 finished` is printed.
11. The final message appears.

The two waits happen one after another, so the program takes approximately four seconds, excluding overhead.

**Key point:** A function call runs in the thread that calls it.

---

# 6. The `threading` Module

Python provides the `threading` module to work with threads.

```python
import threading
```

Some important features include:

- `threading.Thread()` — creates a thread object.
- `threading.Lock()` — creates a lock.
- `threading.current_thread()` — returns the current thread object.
- `threading.main_thread()` — returns the main thread object.
- `threading.active_count()` — counts active threads.

Example:

```python
import threading

print("Current thread:", threading.current_thread().name)
print("Main thread:", threading.main_thread().name)
```

Output:

```text
Current thread: MainThread
Main thread: MainThread
```

---

# 7. Creating a Thread Using a Function

This is one of the most common ways to create a thread.

```python
import threading

def task():
    print("Task is running")

t1 = threading.Thread(target=task)
t1.start()
```

## Explanation of every line

### Step 1: Import the module

```python
import threading
```

This allows us to use Python's threading features.

### Step 2: Define the function

```python
def task():
    print("Task is running")
```

This defines the task. The function has not executed yet.

### Step 3: Create the thread object

```python
t1 = threading.Thread(target=task)
```

- `threading.Thread()` creates a thread object.
- `target=task` specifies which function the thread should execute.
- `t1` refers to the created thread object.
- This line does not start the thread.

### Step 4: Start the thread

```python
t1.start()
```

The `start()` method starts a new thread. Python's threading machinery arranges for the thread's `run()` method to execute, which invokes the target function.

## Internal execution flow

```text
Python program starts
        |
        v
Main thread executes code
        |
        v
task() function is defined
        |
        v
Thread object t1 is created
        |
        v
t1.start() is called
        |
        v
New thread is started or scheduled
        |
        v
New thread executes task()
```

The exact low-level details are handled by Python and the operating system. This diagram shows the important conceptual steps.

**Remember:** Creating a thread object and starting the thread are two different actions.

---

# 8. Why Do We Use `target=task` Instead of `target=task()`?

This is a very important concept.

### Correct

```python
t1 = threading.Thread(target=task)
```

This passes the function itself to the thread.

### Incorrect for the usual thread-target pattern

```python
t1 = threading.Thread(target=task())
```

Here, Python calls `task()` immediately while evaluating the argument. Its return value becomes the target.

If `task()` returns `None`, the thread has no callable target to execute.

Compare:

```python
task       # Refers to the function
task()     # Calls the function immediately
```

**Interview point:** Pass the function object as `target`; do not call it when creating the thread.

---

# 9. What Happens Internally When `start()` Is Called?

Consider this program:

```python
import threading
import time

def task():
    print("Child thread: task started")
    time.sleep(2)
    print("Child thread: task finished")

t1 = threading.Thread(target=task)

t1.start()

print("Main thread: continuing")
```

Possible output:

```text
Child thread: task started
Main thread: continuing
Child thread: task finished
```

Another valid output may print the main-thread message first.

### Step-by-step execution

1. The main thread creates the thread object `t1`.
2. The main thread calls `t1.start()`.
3. Python starts or schedules the new thread.
4. The new thread executes the target function.
5. The main thread does not automatically wait for the new thread to finish.
6. The main thread continues to the next statement.
7. The child thread calls `time.sleep(2)`.
8. The child thread pauses, but the main thread can continue.
9. The child thread resumes and prints its final message.

### Visual execution flow

```text
MAIN THREAD                 CHILD THREAD
------------                ------------
Create t1
t1.start()  --------------> Starts task()
Print main message          Print start message
Continue                    sleep(2)
                            Resume
                            Print finish message
```

The output order depends on scheduling and timing.

**Important:** `start()` starts the thread. It does not wait for the task to finish.

---

# 10. Creating and Running Two Threads

```python
import threading
import time

def task1():
    for i in range(3):
        print("Task 1:", i)
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2:", i)
        time.sleep(1)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both tasks finished")
```

One possible output:

```text
Task 1: 0
Task 2: 0
Task 1: 1
Task 2: 1
Task 1: 2
Task 2: 2
Both tasks finished
```

The task messages may appear in a different order.

## What does interleaving mean?

Interleaving means the operations of multiple threads can appear mixed together.

The program does not guarantee that all Task 1 messages will print before all Task 2 messages.

Both tasks can make progress while the other is sleeping.

---

# 11. Difference Between `start()` and `run()`

These methods are not interchangeable.

## Using `start()`

```python
import threading

def task():
    print("Running in:", threading.current_thread().name)

t1 = threading.Thread(target=task, name="Worker-1")
t1.start()
t1.join()
```

Typical output:

```text
Running in: Worker-1
```

`start()` starts a new thread and arranges for its `run()` method to execute in that thread.

## Calling `run()` directly

```python
import threading

def task():
    print("Running in:", threading.current_thread().name)

t1 = threading.Thread(target=task, name="Worker-1")
t1.run()
```

Typical output:

```text
Running in: MainThread
```

Why?

Because we called `run()` directly from the main thread. We did not start a new thread.

| `start()` | Direct `run()` call |
|---|---|
| Starts a new thread | Does not start a new thread |
| Executes the task in the new thread | Executes the method in the calling thread |
| Used for multithreaded execution | Directly invokes the method |

---

# 12. Passing Arguments Using `args`

Suppose a function needs a name.

```python
import threading

def greet(name):
    print("Hello", name)

t1 = threading.Thread(target=greet, args=("Teja",))
t1.start()
t1.join()
```

Output:

```text
Hello Teja
```

`args` is a tuple of positional arguments.

For one argument, use a trailing comma:

```python
args=("Teja",)
```

Without the comma, `("Teja")` is a string inside parentheses, not a tuple.

### Passing two arguments

```python
import threading

def add(a, b):
    print("Sum:", a + b)

t1 = threading.Thread(target=add, args=(10, 20))
t1.start()
t1.join()
```

Output:

```text
Sum: 30
```

### Passing keyword arguments using `kwargs`

```python
import threading

def introduce(name, city):
    print(name, "is from", city)

t1 = threading.Thread(
    target=introduce,
    kwargs={"name": "Teja", "city": "Nellore"}
)

t1.start()
t1.join()
```

Output:

```text
Teja is from Nellore
```

- `args` passes positional arguments.
- `kwargs` passes keyword arguments.

---

# 13. The `join()` Method

The `join()` method makes the calling thread wait until the specified thread finishes.

```python
import threading
import time

def task():
    time.sleep(2)
    print("Child task finished")

t1 = threading.Thread(target=task)
t1.start()

t1.join()

print("Main task finished")
```

Output:

```text
Child task finished
Main task finished
```

## Internal execution flow

```text
MAIN THREAD                 CHILD THREAD
------------                ------------
t1.start()  --------------> Begins task
t1.join()                   sleep(2)
WAITING                     Resumes
WAITING                     Prints message
WAITING                     Finishes
Continues
Prints main message
```

The main thread waits at `t1.join()` until the child thread finishes.

## What if we do not use `join()`?

```python
t1.start()
print("Main continues")
```

The main thread can print its message without waiting at that point.

However, a non-daemon child thread can still keep the Python process alive until it finishes.

## Using a timeout

```python
t1.join(timeout=1)
```

This waits for at most approximately one second.

A timeout does not stop the worker thread. If it is still running, the calling thread continues.

---

# 14. The `time.sleep()` Function

The `sleep()` function belongs to the `time` module.

```python
import time

print("Start")
time.sleep(2)
print("End")
```

Output:

```text
Start
End
```

There is approximately a two-second pause between the messages.

## How does `sleep()` work with threads?

```python
import threading
import time

def task():
    print("Child: before sleep")
    time.sleep(3)
    print("Child: after sleep")

t1 = threading.Thread(target=task)
t1.start()

print("Main: continues")
t1.join()
```

Possible output:

```text
Child: before sleep
Main: continues
Child: after sleep
```

The child's `sleep()` pauses the child thread, not the main thread.

---

# 15. Finding and Naming Threads

## Find the current thread

```python
import threading

def task():
    print(threading.current_thread().name)

t1 = threading.Thread(target=task, name="DownloadWorker")
t1.start()
t1.join()
```

Output:

```text
DownloadWorker
```

## Find the main thread

```python
import threading

print(threading.main_thread().name)
```

Typical output:

```text
MainThread
```

## Count active threads

```python
import threading

print(threading.active_count())
```

This returns the number of currently alive threads, including the main thread. The exact count depends on which threads are active at that moment.

Thread names are useful when debugging a program with several workers.

---

# 16. Daemon and Non-Daemon Threads

Threads are non-daemon by default.

## Non-daemon thread

```python
import threading
import time

def task():
    time.sleep(2)
    print("Worker finished")

t1 = threading.Thread(target=task)
t1.start()

print("Main code finished")
```

The main thread may finish its own code before the worker finishes. However, the Python process normally stays alive until non-daemon threads finish.

## Daemon thread

```python
import threading
import time

def background_task():
    while True:
        print("Background task running")
        time.sleep(1)

t1 = threading.Thread(target=background_task, daemon=True)
t1.start()

time.sleep(2)
print("Main code finished")
```

A daemon thread does not keep the Python process alive on its own. It may be stopped abruptly when the main program and all non-daemon threads finish.

### Important points

- Non-daemon is the default.
- `daemon=True` marks a thread as a daemon thread.
- Daemon does not mean faster or higher priority.
- Do not depend on daemon threads to save files or finish important work.

---

# 17. Creating a Thread by Inheriting from `threading.Thread`

Another approach is to create a class that inherits from `threading.Thread`.

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        print("Task is running")

t1 = MyThread()
t1.start()
t1.join()
```

Output:

```text
Task is running
```

### How it works

1. `MyThread` inherits from `threading.Thread`.
2. The class overrides `run()` with the task's code.
3. `MyThread()` creates an object.
4. `start()` starts a new thread.
5. Python executes the overridden `run()` method in the new thread.

Do not call `run()` directly if you want to start a separate thread.

### When is this approach useful?

It can be useful when a task needs its own data and methods. For many simple tasks, the function-based approach is shorter and easier to understand.

---

# 18. Passing Data to a Thread Class

We can use `__init__()` to store data in a thread object.

```python
import threading

class GreetingThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.person_name = name

    def run(self):
        print("Hello", self.person_name)

t1 = GreetingThread("Teja")
t1.start()
t1.join()
```

Output:

```text
Hello Teja
```

### Explanation

- `__init__(self, name)` receives the value.
- `super().__init__()` initializes the parent `Thread` class.
- `self.person_name = name` stores the value in the object.
- `run()` uses the stored value.
- `start()` begins execution in a new thread.

---

# 19. What Is Shared Data?

Threads within the same process can access the same Python objects.

Example:

```python
counter = 0
```

If two threads access and modify this counter, they are working with shared data.

Shared data is useful, but simultaneous access can cause problems if operations are not coordinated.

---

# 20. What Is a Race Condition?

A **race condition** occurs when the correctness of a result depends on the timing or order of concurrent operations.

Suppose two threads must each increment a shared counter once.

Conceptually, an increment involves:

1. Reading the current value.
2. Adding one.
3. Storing the new value.

A problematic interleaving could look like this:

```text
Initial counter = 0

Thread A reads counter -> 0
Thread B reads counter -> 0

Thread A calculates 0 + 1 -> 1
Thread B calculates 0 + 1 -> 1

Thread A writes 1
Thread B writes 1

Final counter = 1
```

We wanted `2`, but one increment was lost.

This illustrates the general problem with unsynchronized read-modify-write operations. The exact behavior depends on the operation and Python implementation, so a small counter example may not reproduce the problem on every run.

---

# 21. What Is a Lock?

A **lock** is a synchronization tool that coordinates access to a shared resource.

Imagine a room with one key:

- A worker obtains the key before entering.
- Other workers wait while the key is held.
- The worker releases the key when leaving.
- Another waiting worker may then acquire it.

In Python, create a lock like this:

```python
import threading

lock = threading.Lock()
```

A lock only coordinates threads that use that same lock. It does not automatically protect a variable everywhere in the program.

---

# 22. Using `acquire()` and `release()`

```python
import threading

lock = threading.Lock()

def task():
    lock.acquire()
    try:
        print("Inside protected section")
    finally:
        lock.release()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
```

### Step-by-step execution

1. Thread A calls `lock.acquire()`.
2. If the lock is free, Thread A acquires it.
3. Thread B calls `lock.acquire()`.
4. If Thread A still holds the lock, Thread B waits.
5. Thread A executes the protected section.
6. The `finally` block releases the lock.
7. Thread B can acquire the lock and execute its protected section.

The order in which the threads acquire the lock is not guaranteed.

**Important:** Do not release a lock unless the current thread has acquired it.

---

# 23. Using `with lock:` — Recommended

Python's `with` statement makes lock management easier.

```python
import threading

lock = threading.Lock()

def task():
    with lock:
        print("Inside protected section")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
```

### What happens internally?

1. Execution enters `with lock:`.
2. Python acquires the lock through the lock's context manager.
3. The protected statements execute.
4. When execution leaves the block, Python releases the lock automatically.
5. If an exception occurs inside the block, the lock is still released as the context manager exits.

This is safer and cleaner than manually pairing `acquire()` and `release()`.

---

# 24. Shared Counter Example Using a Lock

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for _ in range(10000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter:", counter)
```

Expected output:

```text
Counter: 20000
```

### Why does the lock help?

- Both threads use the same lock.
- Only one thread at a time executes the protected increment.
- The read-modify-write operation is coordinated.
- `join()` ensures both threads finish before the final value is printed.

The lock must cover the entire operation that needs protection.

---

# 25. Important Lock Rules

1. Threads must use the same lock object to coordinate with each other.
2. A lock protects only the code that actually uses that lock.
3. Prefer `with lock:` in ordinary cases.
4. Keep protected sections as short as practical.
5. Be careful when waiting for another thread while holding a lock that it needs.
6. The order in which waiting threads acquire a lock is not guaranteed.
7. A lock does not automatically make every operation in the program thread-safe.

---

# 26. Important Methods Summary

| Method or concept | Purpose |
|---|---|
| `threading.Thread()` | Creates a thread object |
| `start()` | Starts a new thread |
| `run()` | Contains the thread's task |
| `join()` | Waits for a thread to finish |
| `time.sleep()` | Pauses the calling thread |
| `threading.Lock()` | Creates a lock |
| `acquire()` | Acquires a lock |
| `release()` | Releases a lock |
| `with lock:` | Automatically manages lock acquisition and release |
| `daemon=True` | Marks a thread as a daemon thread |
| `current_thread()` | Returns the current thread object |
| `main_thread()` | Returns the main thread object |
| `active_count()` | Counts currently alive threads |

---

# 27. Common Beginner Mistakes

### Mistake 1: Calling the function instead of passing it

Incorrect for a normal thread target:

```python
threading.Thread(target=task())
```

Correct:

```python
threading.Thread(target=task)
```

### Mistake 2: Forgetting to call `start()`

```python
t1 = threading.Thread(target=task)
```

This creates a thread object but does not start it.

Correct:

```python
t1.start()
```

### Mistake 3: Assuming output order is fixed

Threads can execute in different orders. The exact output order is not guaranteed.

### Mistake 4: Thinking `sleep()` pauses every thread

It pauses only the thread that calls it.

### Mistake 5: Thinking `join()` starts a thread

`start()` starts a thread. `join()` waits for it.

### Mistake 6: Forgetting to release a manually acquired lock

If using `acquire()` directly, ensure the lock is released safely. Prefer `with lock:` when possible.

### Mistake 7: Assuming threads always make CPU-heavy work faster

In standard CPython, the GIL generally limits simultaneous execution of Python bytecode within one interpreter. Multithreading is often most beneficial for I/O-bound work.

---

# 28. Interview Questions and Answers

### 1. What is multithreading?

Multithreading uses multiple threads in one process so that tasks can make progress concurrently.

### 2. What is the difference between a process and a thread?

A process is a running instance of a program with its own process-level memory space. Threads are execution paths within a process and share its memory.

### 3. What is the main thread?

The main thread is the thread that begins executing the top-level code of a normal Python script.

### 4. What does `threading.Thread()` do?

It creates a thread object that can be configured with a target function and arguments.

### 5. Does creating a thread object start the thread?

No. You must call `start()`.

### 6. Why use `target=task` instead of `target=task()`?

`target=task` passes the function itself. `target=task()` calls the function immediately and passes its return value.

### 7. What happens when `start()` is called?

Python's threading machinery starts a new thread and arranges for its `run()` method to execute.

### 8. What is the difference between `start()` and `run()`?

`start()` starts a new thread. Calling `run()` directly executes the method in the current thread.

### 9. What is the purpose of `join()`?

It makes the calling thread wait until the specified thread finishes.

### 10. What does `time.sleep()` do?

It pauses the thread that calls it for approximately the specified duration.

### 11. What is a race condition?

A race condition occurs when the outcome depends on the timing or order of concurrent operations.

### 12. What is a lock?

A lock is a synchronization mechanism that coordinates access to a protected section or shared resource.

### 13. Why is `with lock:` recommended?

It automatically acquires and releases the lock as the block is entered and exited.

### 14. What is a daemon thread?

A daemon thread does not keep the Python process alive on its own and may be stopped when the process exits.

### 15. Is multithreading always faster?

No. Thread management has overhead, and standard CPython's GIL can limit parallel execution of CPU-heavy Python bytecode. Threads are especially useful for I/O-bound tasks.

### 16. How do you pass arguments to a thread?

Use `args` for positional arguments and `kwargs` for keyword arguments.

---

# 29. Practice Programs

Try these programs after studying the explanations.

1. Print the current thread's name.
2. Create one thread that prints numbers from 1 to 5.
3. Create two threads that print different messages.
4. Pass a name to a thread using `args`.
5. Use `join()` to print a final message after a worker finishes.
6. Use `sleep()` in one thread and observe the main thread continuing.
7. Create a class that inherits from `threading.Thread`.
8. Pass a value to the thread class using `__init__()`.
9. Create two threads that increment a shared counter using a lock.
10. Compare `start()` with a direct `run()` call.

---

# Final Summary

- A process is a running instance of a program.
- A thread is an execution path inside a process.
- A normal Python script begins with a main thread.
- `threading.Thread()` creates a thread object.
- `start()` starts a new thread.
- `run()` contains the task; calling it directly does not start a new thread.
- `join()` waits for a thread to finish.
- `sleep()` pauses only the calling thread.
- Threads can share data, which can introduce race conditions.
- Locks coordinate access to shared data.
- Prefer `with lock:` for safe lock management.
- Multithreading is particularly useful for I/O-bound tasks.

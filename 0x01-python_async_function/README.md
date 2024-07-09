# Python - Async

## About me
Hello! I'm a recent graduate from [ALX Africa](https://www.alxafrica.com/), a school that offers comprehensive software engineering programs. Through my education at ALX Africa, I've gained substantial knowledge and hands-on experience in various aspects of software development.

Please note that I am not permitted to share specific **resources**, **tasks detail**, **examples**, or **proprietary information** from ALX Africa. However, I am excited to share my personal projects and the solutions I've developed. While this summary may not cover every detail, it should provide you with a solid understanding of my work and the code I've written. I encourage you to explore, learn, and use these resources freely.

Feel free to connect with me on my professional networks:
- [LinkedIn](https://www.linkedin.com/in/abdelmounaim-malhaoui/)
- [Twitter](https://x.com/abdelmo65183220)

Thank you for visiting my GitHub, and I hope you find my projects insightful and helpful.

**Abdelmounaim Malhaoui**

## Introduction

This project focuses on asynchronous programming in Python, leveraging the asyncio library to run multiple coroutines concurrently. It includes functions to simulate asynchronous tasks with random delays and measure their execution times.  
+ **Some of the requirements for this project:**  
	- All the files should end with a new line.    
	- All the files must be executable.  
	- The first line of all files should be exactly `#!/usr/bin/env python3`.  
	- The code should use the `pycodestyle` style (version 2.5.x).  
	- All the functions and coroutines must be type-annotated.  
	- All modules and functions should have a documentation.  

## Tasks of the project

### Task 0: The basics of async

Write an asynchronous coroutine `wait_random`.  
[File](0-basic_async_syntax.py)

### Task 1: Let's execute multiple coroutines at the same time with async

Import `wait_random` from the previous python file and write an async routine called `wait_n` that takes in 2 int arguments.  
[File](1-concurrent_coroutines.py)

### Task 2: Measure the runtime

Create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)`.  
[File](2-measure_runtime.py)

### Task 3: Tasks

Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that returns a `asyncio.Task`.  
[File](3-tasks.py)

### Task 4: Tasks

Take the code from `wait_n` and alter it into a new function `task_wait_n`.  
[File](4-tasks.py)

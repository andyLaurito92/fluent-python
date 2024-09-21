"""
First important thing to remember: Difference between parallelism and concurrency:

Concurrency -> DEALING with multiple things at once. Example: Having 1 core and
managing multiple tasks at the same time. This is done by the OS Scheduler that
interlaves each task creating what we called multitasking

Parallelism -> DOING multiple things at once. This requires multicore CPUs, multiple
CPUs, GPU or cluster

Difference: Parallelism is a particular type of concurrency. General concurrency doesn't
have to do multiple things at once. Example of this is what we saw in the taxi simulation
in chapter 17 with coroutines

Execution unit -> object that executes code concurrently. Python has 3 kinds of these:
- Procceses
- Threads
- Coroutines
"""

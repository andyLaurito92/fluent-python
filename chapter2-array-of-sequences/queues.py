"""
The .append and .pop methods make a list usable as a stack or a queue (.pop(0) for FIFO)

Problem w/above is that inserting & removing from the head of a list is costly because the entire list must
be shifted in memory

collections.deque --> thread-safe double-ended queue designed for a fast inserting and removing from both ends

Dequeue can be bounded. If a dequeue is full, when adding an item, another is discard from the opposite end. 

NOTE: Dequeue is really optimized for appending and popping from the ends
"""


from collections import deque
dq = deque(range(10), maxlen=10)
dq
dq.rotate(3)

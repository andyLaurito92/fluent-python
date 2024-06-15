"""
This deadlock happens in Cpython because how the garbage collector works.
When the del statement is called on c, given that the reference count of c get's to 0
Cpython tries to delete the object immediately. There are other interpreters that don't do this
making this deadlock something evitable.
"""

import threading

lock = threading.Lock()

class C(object):
    def __del__(self):
        print('getting lock')
        with lock:
            print('releasing lock')
            pass

c = C()
with lock:
    del c

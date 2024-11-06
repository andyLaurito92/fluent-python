import os

class DirectorySize:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()

    def __init__(self, dirname):
        self.dirname = dirname
        

"""
In this example, we show that the lookup is being done
dynamically
"""
current_dir = Directory('chapter14-inheritance')
print(current_dir.size)

current_dir = Directory('chapter03-dictionaries')
print(current_dir.size)


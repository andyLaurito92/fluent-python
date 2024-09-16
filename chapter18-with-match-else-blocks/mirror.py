import sys

class LookingGlass:
    """
    Context manager object that reverse all strings printed
    in the sys.stdout
    """
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        # This is the value bind to the as VARIABLE expression
        return "WEIRDTHINGSHAPPENING"

    def reverse_write(self, text):
        self.original_write(text[::-1])

    # if everything goes well, these 3 values are None
    """
    The 3 arguments receieved are:
     - exc_type: The type of the exception
     - exc_value: The instante of the exception
     - traceback: https://docs.python.org/3/reference/datamodel.html#traceback-objects
    """
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Please do not divide by zero")
            # To tell the interpreter the exception was handled
            return True
        

"""
Note: The 3 arguments received by __exit__ are the same than
ones you get when calling sys.exc_info()

https://docs.python.org/3/library/sys.html#sys.exc_info
"""

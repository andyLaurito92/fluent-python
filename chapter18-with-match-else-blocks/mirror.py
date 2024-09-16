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
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Please do not divide by zero")
            # To tell the interpreter the exception was handled
            return True
        

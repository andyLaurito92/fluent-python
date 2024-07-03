"""
Closures are functions with an extended scope that encompasses nonglobal variables
referenced in the body of the function but not defined there.

Let's see an example of a closure by defining an averager: a higher-order function
that returns a function that computes the average of all arguments passed to it
accumulative

Let's see first the OOP way of doing it
"""

class Averager:
    def __init__(self):
       self.series = []

    def __call__(self, value):
        self.series.append(value)
        total = sum(self.series)
        return total / len(self.series)

avg = Averager()

print(avg(10))
print(avg(11))
print(avg(12))


"""
In contrast, the functional way of doing it is by using a closure
"""

def make_averager():
    series = []

    def averager(value):
        series.append(value)
        total = sum(series)
        return total / len(series)

    return averager

avg_fun = make_averager()
print(avg_fun(10))
print(avg_fun(11))
print(avg_fun(12))

"""
In the above example, series is a free variable of the closure. This means a variable
that is not bound in the local scope. 
"""

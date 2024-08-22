"""
Showing how super works for method resolution when having the diamon problem
in multiple inheritance
"""

class Root:
    def ping(self):
        print(f'{self}.ping() from Root')

    def pong(self):
        print(f'{self}.pong() from Root')

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<instance of {cls_name}>'

class A(Root):
    def ping(self):
        print(f'{self}.ping() from A')
        super().ping()

    def pong(self):
        print(f'{self}.pong() from A')
        super().pong()
        
class B(Root):
    def ping(self):
        print(f'{self}.ping() from B')
        super().ping()

    def pong(self):
        print(f'{self}.pong() from B')

class Leaf(A, B):
    def ping(self):
        print(f'{self}.ping() from Leaf')
        super().ping()


print("Calling ping from leaf")
leaf = Leaf()
leaf.ping()

print("Calling pong from leaf")
leaf.pong()



"""
Why does leaf.pong() doesn't end up calling Root.pong()?. Let's review a bit the MRO
of Leaf.

The MRO of Leaf is: Leaf -> A -> B -> Root -> Object. When we call leaf.pong(), that
activates (following the MRO), A.pong() which calls super. When calling super, we need
to go to our MRO and look for the next class in the MRO chain, which in our case is B. So
A.pong() activates B.pong(). Because B.pong() doesn't call super, the chain stops there.
"""

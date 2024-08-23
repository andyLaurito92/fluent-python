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

class U:
    def ping(self):
        print(f'{self}.ping() from U')
        super().ping()

class LeafUA(U, A):
    def ping(self):
        print(f'{self}.ping() from LeafU')
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


"""
This example shows the dynamic nature of super
"""
print("Calling ping from leafua")
leafua = LeafUA()
leafua.ping()


"""
Why dynamic nature? Bc U does not belong to the hierarchy of A, B, or Root, however,
because U calls super inside it's ping method, A.ping() is called. This is because the
MRO of LeafU is: LeafU -> U -> A -> Root -> Object. When calling leafu.ping(), that
activates (following the MRO), U.ping() which calls super, and so on following the chain.

Then super important: Even though U doesn't inherit from any class, super() in U still
triggers the MRO chain. This is why super is dynamic.
"""

"""
It also means that we cannot call directly u.ping() 
"""

try:
    u = U()
    u.ping()
except Exception as e:
    print(f'Error when calling u.ping(): {e}')


class LeafAU(A, U):
    def ping(self):
        print(f'{self}.ping() from LeafAU')
        super().ping()

print("Calling ping from leafau. U.ping() never gets called")        
leafau = LeafAU()
leafau.ping()

"""
Question: What is the MRO of LeafAU? Why?
"""

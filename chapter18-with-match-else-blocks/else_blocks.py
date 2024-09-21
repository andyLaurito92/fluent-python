"""
Else semantics beyond if: You can use else in while, for and try blocks. The
semantics of else in these blocks is more a "then" than an "else", it's not
"Do this OR do that", it's more a "Do this and THEN, if the condition of the
loop become falsy, DO this"

Let's see some examples
"""

# For statements w/else have usually these pattern
from random import randint

fruits_introduced_by_user = ['orange', 'apple', 'banana', 'grapes']

try:
    for fruit in fruits_introduced_by_user:
        if fruit == 'lemon':
            print("Found it!")
    else:
        raise ValueError("Didn't find my lemon! Was supposed to be here!")
except ValueError as err:
    print(err)


    
def do_sht_dangerous():
    val = randint(1, 100)
    if val < 50:
        raise ValueError("Boom!")
    else:
        print("Not this time")

def normal_life():
    print("Just doing my stuff")

def do_sht_with_exception():
    print("You are not supposed to play with random numbres like that!")


"""
When using an else in a try block, we are aiming to change this type
of code:
"""

try:
    do_sht_dangerous()
    normal_life()
except Exception as e:
    do_sht_with_exception()

"""
for this one:
"""

try:
    do_sht_dangerous()
except:
    do_sht_with_exception()
else:
    normal_life()

"""
In the above code, it's clearer that keep_with_life() is not
the reason why we are putting our code in a try/catch statement +
we are explicitly showing that we are guarding against do_sht_dangerous()
Remember that keep_with_life() will only execute if do_sht_dangerous didn't raise any exception
"""


"""
Example on duck typing vs nominal typing:

Python in runtime would allow the above code to be executed. See how duck
actually knows how to duck, however, because a bird doesn't know how to quack,
a static type checker would throw an error (as mypy does)
"""

class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print("Quack!")

def alert(bird):
    return bird.quack()

def alert_bird(bird: Bird) -> str:
    return bird.quack()

def alert_duck(duck: Duck) -> str:
    return duck.quack()

duck = Duck()

# alert(duck)
# alert_duck(duck)
# alert_bird(duck)

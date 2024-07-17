class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """ Returns programmer representation of vector 2d """
        return f"Vector2D({self.x}, {self.y})"

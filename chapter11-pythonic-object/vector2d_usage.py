from vector2d import Vector2D

def matching_vector(avector: Vector2D) -> None:
    match avector:
        case Vector2D(x=0):
            print("Vector with null x coordinate")
        case Vector2D(y=0):
            print("Vector with null y coordinate")
        case Vector2D(x=3, y=y):
            print(f"Vector has 3 as x and {y} as y coordinate")
        case Vector2D(_, y=3):
            # In order to support this case, vector2d has to has class attribute __match_args__ 
            print(f"y is 3")
            

    
matching_vector(Vector2D(3.0, 4.0))
matching_vector(Vector2D(0, 3))
matching_vector(Vector2D(5, 3))

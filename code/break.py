
from object import Object
class Brick(Object):
    def __init__(self, xy, wh, color, type):
        super().__init__(xy, wh, color, type)




if __name__=="__main__":
    brick = Brick((400, 200), (50, 20), (255, 0, 0), "normal")
    print(brick.get_location_xy_wh())
    print(brick.get_type())
    # Print the name of the class:
    print(brick.__class__.__name__)
    # Print the name of the base class:
    print(brick.__class__.__base__.__name__)

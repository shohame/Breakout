
class Colors():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    CYAN = (0, 255, 255)
    BROWN = (165, 42, 42)
    PINK = (255, 192, 203)
    GRAY = (128, 128, 128)
    LIGHT_BLUE = (173, 216, 230)
    GOLD = (255, 215, 0)
    SILVER = (192, 192, 192)
    BRONZE = (205, 127, 50)

class GameColors():
    BRICK = Colors.RED
    BALL = Colors.WHITE
    PADDLE = Colors.BLUE
    BACKGROUND = Colors.BLACK
    TEXT = Colors.WHITE
    WALL = Colors.GRAY
    POWERUP = Colors.GREEN

class GameDimensions():
    BRICK_WH = (60, 20)
    BALL_WH = (30, 30)
    PADDLE_WH = (100, 10)
    BORDER_THICKNESS = 5
    POWERUP_SIZE = 20
    TEXT_SIZE = 16
    SCREEN_WH = (800, 600)
    WALL_THICKNESS = 10


if __name__ == "__main__":
    print("This is globals.py")
    print(f'Colors.BLACK = {Colors.BLACK}')
    print(f'Colors.WHITE = {Colors.WHITE}')
    print(f'Colors.BRICK = {Colors.BRICK}')




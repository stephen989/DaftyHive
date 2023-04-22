from Infrastructure.TextReader import *
import mouse
from typing import Tuple
import time
class Clicker:
    def __init__(self):
        pass

    def Calibrate(self) -> Tuple[x, y]:
        time.sleep(3)
        this.position = mouse.get_position()
        return position

    def Click(self) -> None:
        mouse.click(button = "left")

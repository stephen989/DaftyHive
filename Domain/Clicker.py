from Infrastructure.TextReader import *
import mouse
from typing import Tuple
import time
class Clicker:
    def __init__(self):
        pass

    def Calibrate(self) -> None:
        time.sleep(3)
        self.position = mouse.get_position()

    def Click(self, status) -> None:
        if status == "off":
            return
        pos = mouse.get_position()
        mouse.move(self.position[0], self.position[1])
        mouse.click(button = "left")
        mouse.move(pos[0], pos[1])

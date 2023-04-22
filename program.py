from Domain.Clicker import Clicker
from Infrastructure.TextReader import TextReader
from Infrastructure.TextWriter import TextWriter
from Infrastructure.Handler import Handler
import time

class Loop:
    def __init__(self):
        pass

    def Run(self):
        self.Handler = Handler()
        self.TextReader = TextReader()
        self.Handler.Run()
        self.Clicker = Clicker()
        self.Clicker.Calibrate()
        print("Running")
        while True:
            status = self.TextReader.Read()
            self.Clicker.Click(status)
            time.sleep(10)

if __name__ == "__main__":
    loop = Loop()
    loop.Run()
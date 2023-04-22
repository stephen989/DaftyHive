import os
class TextReader():
    def __init__(self):
        self.file = os.path.join(os.getcwd(), "status.txt")

    def Read(self)-> str:
        with open(self.file, "r") as file:
            statusString = file.readline().strip()
        return statusString

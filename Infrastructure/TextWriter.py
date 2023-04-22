import os
class TextWriter():
    def __init__(self):
        self.file = os.path.join(os.getcwd(), "status.txt")
        if not os.path.exists(self.file):
            self.Write("on")

    def Write(self, status : str)-> None:
        with open(self.file, "w") as file:
            file.write(status.strip())

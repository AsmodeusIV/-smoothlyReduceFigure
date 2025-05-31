class Progress:
    def __init__(self):
        self.x = 0
    def next(self, dx):
        pass

class ProgressLinear(Progress):
    def __init__(self):
        super().__init__()
    def next(self, dx):
        self.x += dx
        return self.x
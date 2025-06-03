import math

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
        self.x = min(self.x, 1)
        return self.x

class ProgressQuadratic(Progress):
    def __init__(self):
        super().__init__()
    def next(self, dx):
        self.x += dx
        self.x = min(self.x, 1)
        return self.x*self.x

class ProgressTan(Progress):
    def __init__(self):
        super().__init__()
    def next(self, dx):
        self.x += dx
        self.x = min(self.x, 1)
        return min(math.tan(self.x), 1.0001)
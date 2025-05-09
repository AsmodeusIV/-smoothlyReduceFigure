import math

class Figure:
    def __init__(self, x: float, y:float):
        self.centerX = x
        self.centerY = y
        
    def draw(self, canvas):
        pass
    
    def newCenter(self, x, y):
        self.dx = x - self.centerX
        self.dy = y - self.centerY
        self.startX = self.centerX
        self.startY = self.centerY
    
    def reduce(self, procent):
        self.centerX = self.startX+self.dx*procent
        self.centerY = self.startY+self.dy*procent
        
class Circle(Figure):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y)
        self.radius = radius
        self.color = "blue"  
        
    def draw(self, canvas):
        x0 = self.centerX - self.radius
        y0 = self.centerY - self.radius
        x1 = self.centerX + self.radius
        y1 = self.centerY + self.radius
        canvas.create_oval(x0, y0, x1, y1, outline=self.color)
        
    def set_color(self, color: str):
        self.color = color
        
    def reduce(self, procent):
        super().reduce(procent)  
        self.radius = max(0, self.startRadius+self.dr*procent)
    
    def newCord(self, x, y, r):
        super().newCenter(x, y)
        self.dr = r - self.radius 
        self.startRadius = self.radius
        self.newRadius = y
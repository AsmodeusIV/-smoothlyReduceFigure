import tkinter as tk
from figure import Circle, Stone
from ProgressFunc import ProgressLinear, ProgressQuadratic, ProgressTan


class MainWindow:
    def __init__(self, title="redice figures", width=800, height=600):
        self.root = tk.Tk()
        self.root.title(title)
        self.dx = 0.01
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Создаем окружность
        #self.circle = Circle(400, 300, 250)
        #self.circle.newCord(200, 200, 150)
        self.figure = Stone(400,300,250,6)
        self.figure.newCord(200, 200, 150)
        self.progress = 0
        self.progressFunc = ProgressTan()
        
    def animate(self):
        if self.progress <= 1:
            self.canvas.delete("all")
            self.figure.draw(self.canvas)
            self.figure.reduce(self.progress)
            self.progress = self.progressFunc.next(self.dx)

            # Планируем следующий кадр анимации через 16 мс (~60 FPS)
            self.root.after(16, self.animate)
        
    def run(self):
        self.animate()  # Запускаем анимацию
        self.root.mainloop()
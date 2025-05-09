import tkinter as tk
from figure import Circle

class MainWindow:
    def __init__(self, title="redice figures", width=800, height=600):
        self.root = tk.Tk()
        self.root.title(title)
        
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Создаем окружность
        self.circle = Circle(400, 300, 250)
        self.circle.newCord(200, 200, 150)
        self.progress = 0
        
    def animate(self):
        if self.progress <= 1:
            self.canvas.delete("all")
            self.circle.draw(self.canvas)
            self.circle.reduce(self.progress)
            self.progress += 0.01  # Шаг анимации
            
            # Планируем следующий кадр анимации через 16 мс (~60 FPS)
            self.root.after(16, self.animate)
        
    def run(self):
        self.animate()  # Запускаем анимацию
        self.root.mainloop()

# Запуск приложения
if __name__ == "__main__":
    app = MainWindow()
    app.run()
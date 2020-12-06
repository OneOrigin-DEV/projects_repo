from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.id, 0, -1)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height():
            self.y = -1

tk = Tk()
tk.title("Daniel's Pong Game")
tk.resizable(10, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0,)
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

    #update 1





from tkinter import ttk
import tkinter as tk


class Frame:
    def __init__(self, root, xPosition=10, yPosition=10, width=50, height=100, backgroundColor='#3AAFA9'):
        self.root = root
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.width = width
        self.height = height
        self.core = tk.Frame(
            height=self.height,
            width=self.height,
            bd=1,
            background=backgroundColor
        )
        self._place()

    def _place(self):
        self.core.place(x=self.xPosition, y=self.yPosition)

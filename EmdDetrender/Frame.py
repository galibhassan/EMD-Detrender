from tkinter import ttk
import tkinter as tk


class Frame:
    def __init__(self, root, xPosition=10, yPosition=10, width=50, height=100, backgroundColor='#575B82'):
        self.root = root
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.width = width
        self.height = height,
        self.backgroundColor = backgroundColor,
        self.core = tk.Frame(
            height=self.height,
            width=self.width,
            bd=1,
            background=self.backgroundColor
        )
        self._place()

    def _place(self):
        self.core.place(x=self.xPosition, y=self.yPosition)

from tkinter import ttk
import tkinter as tk


class Button:
    def __init__(self, root, windowHeight, xPosition=10, yPosition=10, text="Press it!", backgroundColor='#C56C50', foreground='white', eventHandlers={"click": ""}):
        self.root = root
        self.windowHeight = windowHeight
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.text = text
        self.backgroundColor = backgroundColor
        self.core = tk.Label(
            background=self.backgroundColor,
            foreground=foreground,
            text=self.text,
            font=("", 10),
            padx=20,
            pady=5,
            width=30,
            borderwidth=2,
            # relief="groove"
        )
        self._place()
        self._activateEventListeners()

    def _place(self):
        self.core.place(
            x=self.xPosition,
            y=self.yPosition
        )

    def _activateEventListeners(self):
        # event listner
        self.core.bind('<ButtonPress>', self.handleButtonClick)
        self.core.bind('<Enter>', self.handleButtonHover)
        self.core.bind('<Leave>', self.handleButtonLeave)

    def handleButtonClick(self, event):
        self.core["background"] = '#5689ED'

    def handleButtonHover(self, event):
        self.core["background"] = '#ED7A56'

    def handleButtonLeave(self, event):
        self.core["background"] = self.backgroundColor

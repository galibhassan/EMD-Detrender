from tkinter import ttk
import tkinter as tk


class CheckButtons:
    def __init__(self, imfCount, root, background="#575B82"):
        self.root = root
        self.imfCount = imfCount
        self.background = background
        self.checkButtonValues = []

        self.getCheckButtons(imfCount, self.root)

    def getCheckButtons(self, count, root):
        checkButtons = []
        for i in range(count):
            self.checkButtonValues.append(tk.IntVar())

        for i in range(count):
            checkButtonArrElement = {
                "value": tk.IntVar(),
                "main": tk.Checkbutton(
                    root,
                    text=f'IMF {i}',
                    font=("", 12),
                    background=self.background,
                    foreground="#818BE9",
                    variable=self.checkButtonValues[i],
                    relief="flat"
                )
            }
            checkButtons.append(checkButtonArrElement)

        # display all the checkButtons
        for i in range(len(checkButtons)):
            checkButtons[i]["main"].place(x=0, y=i*30)

    def getCheckButtonValues(self):
        _output = []
        for i in range(len(self.checkButtonValues)):
            _output.append(self.checkButtonValues[i].get())
        return _output

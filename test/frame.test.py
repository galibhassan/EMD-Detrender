import sys
sys.path.append("../EmdDetrender")
import tkinter as tk
from EmdDetrender.Frame import Frame
from EmdDetrender.sampleClass import MyClass

root = tk.Tk()

myFrame = Frame(root)

root.mainloop()
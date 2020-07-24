from tkinter import ttk
import tkinter as tk
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use("TkAgg")
from .Frame import Frame


class EMDGraphics:
    root = tk.Tk()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    ratio_monitorToAppwindow = 1.5
    windowWidth = int(screenWidth/ratio_monitorToAppwindow)
    windowHeight = int(screenHeight/ratio_monitorToAppwindow)
    offsetX = int(screenWidth/2 - windowWidth/2)
    offsetY = int(screenHeight/2 - windowHeight/2)
    dpi = 100
    sideBarWidth=300
    figWidth = (windowWidth - sideBarWidth)/dpi
    figHeight = (windowHeight)/dpi
    sideBar = Frame(root, 0, 0, width=sideBarWidth, height=windowHeight)
    
    def __init__(self, domain, timeSeries, title="EMD Detrender"):
        self.timeSeries = timeSeries
        self.domain = domain
        self.root.geometry(f"{self.windowWidth}x{self.windowHeight}+{self.offsetX}+{self.offsetY}")
        self.root.title(title)


    def makeFigure(self):
        fig = Figure(figsize=(self.figWidth, self.figHeight), dpi=self.dpi)
        ax = fig.add_subplot(111)
        ax.plot(self.domain, self.timeSeries, color='#3AAFA9')
        return fig





    def show(self):
        fig = self.makeFigure()
        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().place(x=self.sideBarWidth, y=0)
        self.root.mainloop()
    

from PyEMD import EMD
import numpy as np
from tkinter import ttk
import tkinter as tk
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use("TkAgg")
from Frame import Frame

def emdDetrender(timeSeries, domain):
    # define root
    root = tk.Tk()

    # define relevent params
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

    root.title("EMD Detrender")
    root.geometry(f"{windowWidth}x{windowHeight}+{offsetX}+{offsetY}")

    IMFs = getIMFs(timeSeries)

    # make plot
    nRowsPlot = len(IMFs)
    nColsPlot = 1
    fig = Figure(figsize=(figWidth, figHeight), dpi=dpi)
    ax = fig.add_subplot(nRowsPlot, nColsPlot, 2)
    ax.plot(domain, timeSeries, color='#3AAFA9')

    # add graphics to the tkinter window
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()

    # place UI components in tkinter window
    canvas.get_tk_widget().place(x=sideBarWidth, y=0)
    root.mainloop()


def getIMFs(timeSeries):
    emd = EMD()
    IMFs = emd(timeSeries)
    return IMFs


def main():
    domain = np.arange(-6, 6, 0.1)
    timeSeries = np.sin(domain)
    emdDetrender(timeSeries, domain)

main()
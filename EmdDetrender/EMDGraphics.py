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
from Button import Button

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
    print(screenWidth)
    sideBarWidth= int(0.25*windowWidth)
    figWidth = (windowWidth - sideBarWidth)/dpi
    figHeight = (windowHeight)/dpi
    sideBar = Frame(root, 0, 0, width=sideBarWidth, height=windowHeight)

    root.title("EMD Detrender")
    root.geometry(f"{windowWidth}x{windowHeight}+{offsetX}+{offsetY}")

    IMFs = getIMFs(timeSeries)
    fig = plotTimeSeriesAndIMFs(domain, timeSeries, IMFs, figWidth, figHeight, dpi)
    # add graphics to the tkinter window
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()

    # place UI components in tkinter window
    canvas.get_tk_widget().place(x=sideBarWidth, y=0)

    buttonText = "Detrend using selected IMFs"
    button = Button(root, windowHeight, xPosition=10, yPosition=windowHeight-45,  text=buttonText)

    root.mainloop()


def getIMFs(timeSeries):
    emd = EMD()
    IMFs = emd(timeSeries)
    return IMFs

def plotTimeSeriesAndIMFs(domain, timeSeries, IMFs, figWidth, figHeight, dpi):
    # make plot
    nPlotsBeforeIMFs = 1 # for the timeseries itself
    nRowsPlot = len(IMFs) + nPlotsBeforeIMFs
    nColsPlot = 1
    fig = Figure(figsize=(figWidth, figHeight), dpi=dpi)
    
    # plot the timeSeries
    ax = fig.add_subplot(nRowsPlot, nColsPlot, 1)
    ax.plot(domain, timeSeries, color='#3AAFA9')

    # plot the IMFs
    for i in range(len(IMFs)):
        ax = fig.add_subplot(nRowsPlot, nColsPlot, i+1+nPlotsBeforeIMFs)
        ax.set_title(f"IMF {i}", x=-.09, y=0.3, fontsize=10)
        ax.plot(domain, IMFs[i])

    return fig

def main():
    domain = np.arange(-10, 10, 0.02)
    linTrend = 1*domain
    amp = 2
    freq = 2
    noise = np.random.normal(0, 1, len(domain))
    timeSeries = amp*np.sin(freq*domain) + 1.5*np.sin(15*domain) + linTrend
    emdDetrender(timeSeries, domain)

main()

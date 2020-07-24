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
from CheckButtons import CheckButtons

def emdDetrender(timeSeries, domain):
    # define a global
    GLOBAL_DICT = {
        "checkButtonsState": []
    }

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
    sideBarWidth= int(0.25*windowWidth)
    figWidth = (windowWidth - sideBarWidth)/dpi
    figHeight = (windowHeight)/dpi
    sideBar = Frame(root, 0, 0, width=sideBarWidth, height=windowHeight)

    root.title("EMD Detrender")
    root.geometry(f"{windowWidth}x{windowHeight}+{offsetX}+{offsetY}")

    # calculate IMFs, initiate figure
    IMFs = getIMFs(timeSeries)
    fig = plotTimeSeriesAndIMFs(domain, timeSeries, IMFs, figWidth, figHeight, dpi)

    # add graphics to the tkinter window
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()

    # place UI components in tkinter window
    canvas.get_tk_widget().place(x=sideBarWidth, y=0)

    # initiate checkBoxes
    imfCheckboxContainer = Frame(sideBar, xPosition=100, yPosition=100, width=100, height=windowHeight-200, )
    imfCheckButtons = CheckButtons(len(IMFs), imfCheckboxContainer.core)


    # initiate button for detrending
    def buttonClickHandlerCB(args):
        # args is instance of CheckButtons class
        vals = args.getCheckButtonValues()
        GLOBAL_DICT["checkButtonsState"] = vals
        root.destroy()

    buttonText = "Detrend using selected IMFs"
    button = Button(
        root, 
        windowHeight,
        clickHandler={
            "callback": buttonClickHandlerCB,
            "args": imfCheckButtons
        }, 
        xPosition=10, 
        yPosition=windowHeight-45,  
        text=buttonText
    )

    appHeading = tk.Label(
        text= 'EMD Detrending',
        font=("", 14),
        background='#4D4F68',
        foreground='white',
        padx=30,
        pady=10,
        width=23
    )
    appHeading.place(x=0, y=0)

    root.mainloop()
    return GLOBAL_DICT["checkButtonsState"]

    

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
        ax.set_title(f"IMF {i}", x=-.09, y=0.3, fontsize=12)
        ax.plot(domain, IMFs[i])

    return fig

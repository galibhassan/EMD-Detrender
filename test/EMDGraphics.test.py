import sys
sys.path.append("../EmdDetrender")
import tkinter as tk
from EmdDetrender.Frame import Frame
from EmdDetrender.EMDGraphics import EMDGraphics
import numpy as np


x = np.arange(-6, 6, 0.1)
y = np.sin(x)
myEMDGraphics = EMDGraphics(x,y)
myEMDGraphics.show()

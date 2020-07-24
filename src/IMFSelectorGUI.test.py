import numpy as np
from IMFSelectorGUI import emdDetrender
from matplotlib import pyplot as plt

def main():
    domain = np.arange(-10, 10, 0.02)
    linTrend = 1*domain
    amp = 2
    freq = 2
    noise = np.random.normal(0, 1, len(domain))
    timeSeries = amp*np.sin(freq*domain) + 1.5*np.sin(15*domain) + linTrend + noise
    
    # plot the timeseries
    plt.plot(domain, timeSeries)
    plt.title("Main Timeseries")
    plt.show()
    
    # test emdDetrender
    detrendedTimeSeries = emdDetrender(timeSeries, domain)

    plt.plot(domain, timeSeries, label="Main timeseries")
    plt.plot(domain, detrendedTimeSeries, linewidth=3, label="Selected IMFs-removed")
    plt.legend(loc='lower right')
    plt.show()
    
main()

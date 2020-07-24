import numpy as np
from IMFSelectorGUI import emdDetrender
from matplotlib import pyplot as plt

def main():
    domain = np.arange(-10, 10, 0.02)
    linTrend = 1*domain
    amp = 2
    freq = 2
    noise = np.random.normal(0, 1, len(domain))
    timeSeries = amp*np.sin(freq*domain) + 1.5*np.sin(15*domain) + linTrend

    # test emdDetrender
    detrendedTimeSeries = emdDetrender(timeSeries, domain)

    plt.plot(domain, timeSeries)
    plt.plot(domain, detrendedTimeSeries)
    plt.show()

main()

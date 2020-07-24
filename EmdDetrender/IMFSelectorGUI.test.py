import numpy as np
from IMFSelectorGUI import emdDetrender

def main():
    domain = np.arange(-10, 10, 0.02)
    linTrend = 1*domain
    amp = 2
    freq = 2
    noise = np.random.normal(0, 1, len(domain))
    timeSeries = amp*np.sin(freq*domain) + 1.5*np.sin(15*domain) + linTrend

    # test emdDetrender
    selectedIMFs = emdDetrender(timeSeries, domain)
    print(selectedIMFs)

main()
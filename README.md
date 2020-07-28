# EMD Detrender
Given a timeseries data, this package
- performs Empirical Mode Decomposition(EMD) on the timeseries,
- provides the user a simple graphical user interface to choose the Imperical Mode Functions (IMF)
- and finally, detrend the timeseries by subtracting the selected IMFs.

## Demo
![IMFSubtractorGif](https://raw.githubusercontent.com/galibhassan/images/master/EmdDetrender%2002.gif)

## API
- #### `emdDetrender`
    input: <br>
    - `timeseries`: a `numpy` 1d array <br>
    - `domain`: a `numpy` 1d array <br>
    
    output: <br>
    - `detrendedtimeseries`: a `numpy` 1d array <br>

# Component Specification

## Software Components
![](components.png)

### Raw Data
- Functions: 
    - accumulate all streams of election and demographic data, for all intended years
- Input: 
    - all unchanged .CSV files from MIT and the Census Bureau
- Output: 
    - all .CSV files, renamed for clarity and organization
### Data Processor
- Functions: 
    - load raw data
    - handle malformed values
    - merge election and demographic data by year and state
    - reformat for scipy modeling 
- Input: 
    - all labeled .CSV files
- Output: 
    - processed .CSV file
### Modeling
- Functions: 
    - load formatted data
    - for each year's worth of data, apply clustering
    - attach cluster labels and descriptive statistics to all records
- Input: 
    - consolidated and cleaned .CSV file
- Output: 
    - DataFrame or ndarray representation of modeled data 
### Map Manager
- Functions: 
    - filter modeled data per user interaction requests from web visualization
    - generate bokeh map views based on filters
    - transmit rendered bokeh visualization to browser
- Input: 
    - modeled data as pandas.DataFrame or numpy.ndarray
- Output: 
    - bokeh visualization (Python objects, functions, and code) 
### Output
- Functions:
    - render requested bokeh visualization from Map Manager
    - accept requests based on user interactions with point-and-click map interface
    - transmit new requests to Map Manager
- Input: 
    - bokeh visualization
- Output: 
    - HTML rendering of bokeh map 

## Interactions

## Preliminary Plan 

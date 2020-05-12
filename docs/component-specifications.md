# Component Specification

## Software Components
![](components.png)

### Raw Data
- Function: accumulate all streams of election and demographic data, for all intended years
- Input: all unchanged .CSV files from MIT and the Census Bureau
- Output: all .CSV files, renamed for clarity and organization
### Data Processor
- Function: load raw data, handle malformed values, merge election and demographic data by year and state, reformat for scipy modeling 
- Input: all labeled .CSV files
- Output: processed .CSV file
### Modeling
- Function: load formatted data, apply clustering (for a given year's worth of data), apply cluster label to each record in that year
- Input: consolidated and cleaned .CSV file
- Output: DataFrame or ndarray representation of processed data, now with new feature denoting each state's grouping in a given year
### Map Manager
- Function: request
- Input:
- Output:
### Output
- Function:
- Input:
- Output:

## Interactions

## Preliminary Plan 

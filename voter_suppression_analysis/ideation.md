## Streams of Data

[*Election Results*](https://electionlab.mit.edu/data)

[*Demographics*](https://www.census.gov/data/tables/time-series/demo/voting-and-registration/congressional-voting-tables.html)

[*Turnout*](https://www.census.gov/data/tables/time-series/demo/voting-and-registration/p20-583.html)

## General Approach(es)

1. We treat this as a data science problem (still concluding in a map visualization):
    * analysis only
        - significant differences between populations (meaning geographical areas)
    * modelling
        - clustering based on joined data: results + turnout + demographics 
        - if using 2018 results (most recent), what to predict on?

2. We treat this exclusively as a visualization task: 
    * map all variables of interest geographically
        - political victories
        - population attributes
        - turnout and registration

3. Other suggestions? 

## Other Tidbits

- the biggest part of "suppression" are the missing "suppressing" variables, which may include
    * region-by-region registration laws (punitive ID laws, costs, etc.)
    * poll location/volunteer scarcity 
    * holiday/time-off status of voting days 
    * US territories that don't have voting rights lmao?
- desired granularity is at the congressional district level, but may be compromised to the state level
- further selection/organizing in the data is required








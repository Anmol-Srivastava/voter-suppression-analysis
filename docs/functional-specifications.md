# Functional Specification

## Background

The results of American elections seem to matter now more than ever. Incredible amounts of time, money, and effort are spent in the analysis and prediction of voter behavior, as low turnout and unexpected voting patterns become the downfall of political candidates and parties. But little attention is given to the closely-related issue of voter suppression: the combination of factors that hinder every citizen’s ability to vote freely.

It can be difficult to completely encapsulate every instance of voter suppression. Sound arguments attribute many factors to inhibited turnout. Some are easily measured, such as constituency wealth, polling location sparsity, or population demographics. Others are harder to quantify, like wait times, insufficient staffing, and malicious ID laws. Such simple and complex factors are included (or at least acknowledged) in our project. There are issues outside of the scope of this project, too: namely, the absent voting rights of populations that live in US “territories.”

Our project aims to analyze potential contributors to voter suppression across the U.S., and provide users with an interactive visualization describing the same. The visualization will primarily be composed of a navigable map; accompanying labels and statistics will contextualize the information summarized by this map. Importantly, our project aims to help users recognize, explore, and compare the degree of voter suppression across the U.S, on a constituency-by-constituency basis.

## User Profiles

Anticipated users are any lay-people interested in learning about the factors inhibiting voter turnout, or the variation in voting experiences across the U.S. Users may also be state-level legislators in charge of the redistricting process. These policy-makers need a good understanding of the citizen populations in each constituency to carry out this role. To that end, the data represented in our visualization may also be useful. 

In any case, users should be able to navigate map applications resembling those found on popular websites (e.g., Google Maps) via hover, point-and-click, pan, and scrolling operations. Given appropriate direction, they must be able to clone a Git repository and run Python scripts to access and launch our visualization. 

## Data Sources

- [Official Returns for the 2018 Midterm Elections](https://github.com/MEDSL/2018-elections-official)
    - Provider: MIT Election Lab
    - Structure: Redundant .CSV files representing the same data, for each regional granularity (state, county, district, and precinct). Attributes of interest include:
        - office
        - party 
        - stage 
        - votes 
- [Voting and Registration in the Election of November 2018](https://www.census.gov/data/tables/time-series/demo/voting-and-registration/p20-583.html)
    - Provider: U.S. Census Bureau
    - Structure: Distinct .CSV files, each quantifying the rate of voter turnout among some central target demographic. Interesting demographics (each with their own file) include:
        - race
        - age
        - sex
        - income/worker status
    - Notes:
        - each file has two primary variable types: percent registered to vote, and percent voted
        - additional files recording voting method, and reasons for not voting, were also used
- [Shapefiles for US Congressional Districts LINK MISSING](https://www.google.com)
    - Provider: Missing
    - Structure: Missing 

## Use Cases

Hee.

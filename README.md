# Voter Suppression Analysis

[![Build Status](https://travis-ci.com/Anmol-Srivastava/voter-suppression-analysis.svg?branch=master)](https://travis-ci.com/Anmol-Srivastava/voter-suppression-analysis)
[![GitHub contributors](https://img.shields.io/github/contributors/Anmol-Srivastava/voter-suppression-analysis)](#contributors)
[![GitHub license](https://img.shields.io/github/license/Anmol-Srivastava/voter-suppression-analysis)](./LICENSE)
[![Coverage Status](https://coveralls.io/repos/github/Anmol-Srivastava/voter-suppression-analysis/badge.svg?branch=packaging)](https://coveralls.io/github/Anmol-Srivastava/voter-suppression-analysis?branch=packaging)

## Overview

*This project is part of an assignment for [DATA 515: Software Engineering for Data Scientists](http://uwseds.github.io).*

The aim of this project is to visualize the state of voter suppression across the US. Chiefly, this project draws on data from the US Census Bureau and the American Civil Liberties Union (ACLU), to create an interactive geographical depiction of voter turnout among various demographics. The central dashboard describes, over several years, each state's turnout by race, sex, and age. This information is accompanied by a visual demarcation of the punitive quality of each state's voting laws. For data-related or other practical reasons, many considerations are left out (*e.g.,* missing income data, or the absent voting rights of US territories). 

Our hope is that this dashboard draws attention to suppressed communities, while encouraging viewers to think critically about any and all factors that inhibit turnout: from voting location sparsity, to misleading, media-disseminated poll results. 

## Installation

*Please note:* 
  - the following steps are intended for a Linux environment
  - counterparts for other environments were not part of the initial scope, and are currently unavailable
  - SOMETHING ABOUT WHICH STEPS ARE ONE-TIME :0

#### Clone and access the repository in a location of your choice:
```
git clone https://github.com/Anmol-Srivastava/voter-suppression-analysis.git
cd voter-suppression-analysis
```

#### Set up and activate the necessary environment: 
```
help
```

#### Launch the dashboard:
```
im in danger
```

## Structure

- `docs`: early-stage functional and component specifications, technology reviews, presentations, and `pylint` test outputs
- `examples`: Jupyter notebook guides for launching and exploring the visualization
- `voter_suppression_analysis`: main module 
  - `data`: raw and sanitized data, with an addtional `README`, and data-processing python script
  - `figures`: mid-development figures and visualization-defining python script 
  - `tests`: python scripts for testing data cleaning and visualization steps, as well as `pylint` integration 

## Team

This project was developed by the following team of graduate students in the UW Master's in Data Science (MSDS) program:

- [Andres De La Fuente](https://github.com/Oponn-1)
- [Anmol Srivastava](https://github.com/Anmol-Srivastava)
- [Juan Solorio](https://github.com/JUAN-SOLORIO)

## License

This project is categorized under the [MIT](./LICENSE) license. 

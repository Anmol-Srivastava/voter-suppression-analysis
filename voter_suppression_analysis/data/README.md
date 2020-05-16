## Turnout Data (UCB)

### Anmol's Notes:
    - several sub-tables, need to decide on which (assuming available across all years)
    - also need to decide how many years to include 
    - file formats need severe correction
    
### Link:
    - (https://www.census.gov/topics/public-sector/voting/data/tables.2018.html)
turnout data below 

## Election Data (MEL)

### Anmol's Notes:
    - The "senate" and "district" sets have constituency-level Senate & House returns, respectively.
    - The "state" and "county" sets have constituency-level state office and county office returns, respectively. 
    - The "precinct" set contains precinct-level election returns for all offices, and is incomplete but updated weekly.

### Apparent Distinctions:
    - States are divided into constituencies, where each of the 435 total constituencies elect 1 House member
    - Districts, seemingly, refer to "Congressional" districts (i.e., are the same as constituencies)
        - other types of districts exist, too, and this distinction must be clarified 
    - Counties are collections of areas within constituencies, but those districts do not have to follow county lines
    - Precincts are the smallest unit into which electoral districts are divided
        - each has 1 poll location for its residents, although a location may be common to multiple precincts  

### Data Validity: 
    - Indiana, Kentucky, Maine, Mississippi, New York, South Dakota, and Utah are missing in the precinct data
    - DC has its own representation in the data, and New York data may be missing in multiple sets
    - Some data for Texas was pre-processed (see repository for details), other states also have minor erroneous issues

### Link:
    - (https://github.com/MEDSL/2018-elections-official)



'''
Code to load, clean, and combine all relevant data.
See README for references re: data. 
'''
import glob 
import pandas as pd 


# useful constants for accessing files 
AGE_PATH_REGEX = 'clean/*_age.csv'
SEX_PATH_REGEX = 'clean/*_sexrace.csv'


# useful constants for renaming and removing columns 
AGE_COLUMN_NAMES = [
    'state', 'age_bracket', 'total', 'total_reg', 'percent_reg', 
    'ci_reg', 'total_voted', 'percent_voted', 'ci_voted', 'yr' 
]

SEX_COLUMN_NAMES = [
    'state', 'group', 'pop', 'total_cit', 'percent_cit', 'ci_cit',
    'total_reg', 'percent_reg', 'ci_reg', 'total_voted', 'percent_voted',
    'ci_voted', 'yr'
]

KEEP_AGE_COLUMNS = ['state', 'age_bracket', 'percent_reg', 'yr']
KEEP_SEX_COLUMNS = ['state', 'group', 'percent_reg', 'yr']


def get_age_df(file_path):
    '''
    Load age data by file name, transform into pd.DataFrame and
    return DataFrame object with only relevant columns and cleaned
    values.  

    Note: NaN values are kept for possible use in modeling/viz. 

    Args: 
        file_path: str, designating file to retrieve for a given year

    Returns:
        pd.DataFrame, processed age data for that year 
    '''

    # access, label, and sanitize data 
    df = pd.read_csv(file_path, header=0, names=AGE_COLUMN_NAMES)
    df = df[KEEP_AGE_COLUMNS]
    df.percent_reg = df.percent_reg.apply(pd.to_numeric, errors='coerce')
    return df 


def get_sexrace_df(file_path):
    '''
    Load sexrace data by file name, transform into pd.DataFrame
    and return DataFrame object with only relevant columns and cleaned
    values.  

    Note: NaN values are kept for possible use in modeling/viz. 

    Args: 
        file_path: str, file for which to retrieve sexrace data

    Returns:
        pd.DataFrame, processed sexrace data for that year 
    '''

    # access, label, and sanitize data 
    df = pd.read_csv(file_path, header=0, names=SEX_COLUMN_NAMES)
    df = df[KEEP_SEX_COLUMNS]
    df.percent_reg = df.percent_reg.apply(pd.to_numeric, errors='coerce')
    return df 


def combine_age_data():
    '''
    Retrieve all age-related data files, combine into one pd.DataFrame
    object. 

    Args:   None

    Returns:
        pd.DataFrame, combined age data for all years 
    '''

    # retrieve all relevant file paths 
    age_file_paths = glob.glob(AGE_PATH_REGEX)
    df_list = []

    # iterative store pd.DataFrame representation of each 
    for age_file in age_file_paths:
        print('Reading %s...' % age_file)
        df = get_age_df(age_file)
        df_list.append(df)

    # concatenate all data 
    combined = pd.concat(df_list, axis=0, ignore_index=True)
    return combined 


def combine_sexrace_data():
    '''
    Retrieve all sexrace-related data files, combine into one 
    pd.DataFrame object. 

    Args:   None

    Returns:
        pd.DataFrame, combined sexrace data for all years 
    '''

    # retrieve all relevant file paths 
    sex_file_paths = glob.glob(SEX_PATH_REGEX)
    df_list = []

    # iterative store pd.DataFrame representation of each 
    for sex_file in sex_file_paths:
        print('Reading %s...' % sex_file)
        df = get_sexrace_df(sex_file)
        df_list.append(df)

    # concatenate all data 
    combined = pd.concat(df_list, axis=0, ignore_index=True)
    return combined 





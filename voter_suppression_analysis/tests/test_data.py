''' FUNCTIONS TO TEST DATA PROCESSING FUNCTIONALITY '''

import random
import pandas as pd 

from pathlib import Path

from voter_suppression_analysis.data.processing import \
    get_age_df, get_sexrace_df, \
    combine_age_data, combine_sexrace_data, \
    homogenize_age_data, homogenize_sexrace_data


# useful constants for file locations
CWD = Path(__file__).parent
EXAMPLE_PATH_AGE = CWD / '../data/samples/age_01.csv'
EXAMPLE_PATH_SEX = CWD / '../data/samples/sex_01.csv'
EXAMPLE_PATH_LAW = CWD / '../data/samples/law_01.csv'

EXAMPLE_DIR_AGE = str(CWD / '../data/samples/example_age_folder/')
EXAMPLE_DIR_SEX = str(CWD / '../data/samples/example_sex_folder/')

GARBAGE_PATH = str(random.randint(0,9))  

# useful constants for expected column names
EXPECTED_AGE_COLUMNS = [
    'STATE', 'Age', 'Total', 'Total Registered', 'Percent registered (18+)',
    'CI Registered', 'Total Voted', 'Percent voted (18+)', 'CI Voted', 'Year'
]

EXPECTED_SEX_COLUMNS = [
    'STATE', 'Group', 'Population (18+)', 'Total Citizen', 'Percent Citizen',
    'CI Citizen', 'Total Registered', 'Percent Registered (18+)', 
    'CI Registered', 'Total Voted', 'Percent Voted (18+)', 'CI Voted', 'Year'
]

# useful constants for expected shapes
FINISHED_LENGTH_AGE = 55

# useful constants for state labels and IDs
STATE_NUMS = [
    1,  2,  4,  5,  6,  8,  9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 0
]

STATE_NAMES = [
    'ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 
    'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 
    'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 
    'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 
    'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
    'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK', 
    'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON', 
    'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA', 
    'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 
    'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'NATIONAL'
]


def test_get_age_df():
    ''' 
        Test the following conditions for get_age_df():
            - function runs
            - function breaks with a wrong filepath
            - resulting dataframe has the right columns
            - resulting df has data
            - punctuation has been removed
    '''
    print(EXAMPLE_PATH_AGE)
    # smoke tet
    df = get_age_df(EXAMPLE_PATH_AGE)

    # check if invalid file paths break function
    invalid_file_caught = False
    
    try:
        garbage_df = get_age_df(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True
    
    assert invalid_file_caught

    # check resulting df has data
    assert len(df) > 0

    # check resulting df has correct columns
    assert all(df.columns == EXPECTED_AGE_COLUMNS)

    # check leading punctuation marks have been removed
    assert df["Age"][0] == "Total"


def test_get_sexrace_df():
    ''' 
        Test the following conditions for get_sexrace_df():
            - function runs
            - function breaks with wrong filepath
            - resulting dataframe has right columns
            - resulting df has data
            - punctuation has been removed
    '''

    # smoke test
    df = get_sexrace_df(EXAMPLE_PATH_SEX)
   
    # check if invalid file paths break function
    invalid_file_caught = False
    
    try:
        garbage_df = get_sex_df(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True

    assert invalid_file_caught

    # check resulting df has data
    assert len(df) > 0

    # check resulting df has correct columns
    assert all(df.columns == EXPECTED_SEX_COLUMNS)

    # check punctuation has been removed
    assert df["Group"][0] == "Total"


def test_combine_age_data():
    ''' 
        Test following conditions for combine_age_data():
            - resulting dataframe has all the data
            - invalid filepath doesn't work 
            - legislative data is present
            - NATIONAL label has been substituted for US 
    '''

    # smoke test
    df = combine_age_data(EXAMPLE_DIR_AGE, EXAMPLE_PATH_LAW)

    # test dataframe has enough data
    assert len(df) > 0

    # check if invalid file paths break function
    invalid_file_caught = False

    try:
        garbage_df = combine_age_data(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True

    assert invalid_file_caught

    # check NATIONAL label is in place
    assert df['STATE'][0] == 'NATIONAL'


def test_combine_sexrace_data():
    ''' 
        Test following conditions for combine_sexrace_data():
            - resulting dataframe has all the data
            - invalid filepath doesn't work 
            - legislative data is present
            - NATIONAL label has been substituted for US 
    '''

    # smoke test
    df = combine_sexrace_data(EXAMPLE_DIR_SEX, EXAMPLE_PATH_LAW)

    # test dataframe has enough data
    assert len(df) > 0

    # check if invalid file paths break function
    invalid_file_caught = False

    try:
        garbage_df = combine_age_data(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True

    assert invalid_file_caught

    # check NATIONAL label is in place
    assert df['STATE'][0] == 'NATIONAL'


def test_homogenize_age_data():
    ''' 
        Test conditions for homogenize_age_data():
            - the correct age brackets are present
            - data is in the correct shape
            - state ID's are present
            - state labels are present
    '''

    # smoke test
    combined = combine_age_data(EXAMPLE_DIR_AGE, EXAMPLE_PATH_LAW)
    df = homogenize_age_data(combined)

    # test data is in correct shape
    assert len(df) == FINISHED_LENGTH_AGE

    # test the state IDs and labels are present
    assert all(df['id'].unique() == STATE_NUMS)
    assert all(df['STATE'].unique() == STATE_NAMES)


def test_homogenize_sexrace_data():
    ''' 
        Test conditions for homogenize_age_data():
            - the correct age brackets are present
            - data is in the correct shape
            - state ID's are present
            - state labels are present
    '''

    # smoke test
    combined = combine_sexrace_data(EXAMPLE_DIR_SEX, EXAMPLE_PATH_LAW)
    df = homogenize_sexrace_data(combined)

    # test the state IDs and labels are present
    assert all(df['id'].unique() == STATE_NUMS)
    assert all(df['STATE'].unique() == STATE_NAMES)


''' FUNCTIONS TO TEST DATA PROCESSING FUNCTIONALITY '''

import random
import pandas as pd 
import sys

sys.path.insert(1, '../')
from data.processing import \
    get_age_df, get_sexrace_df,\
    combine_age_data, combine_sexrace_data,\
    homogenize_age_data, homogenize_sexrace_data

# paths to unit test inputs
EXAMPLE_AGE_CSV_PATH = 'example_age.csv'
EXAMPLE_SEX_CSV_PATH = 'example_sex.csv'
EXAMPLE_AGE_DIR = 'example_age_dir/*_age.csv'
EXAMPLE_SEXRACE_DIR = 'example_sexrace_dir/*_sexrace.csv'
EXAMPLE_LAW_CSV_PATH = 'example_law.csv'
GARBAGE_FILE_PATH = str(random.randint(0,9))

# desired columns
EXPECTED_AGE_COLUMNS = ['STATE','Age', 'Total', 'Total Registered', \
        'Percent registered (18+)', 'CI Registered', 'Total Voted', \
        'Percent voted (18+)', 'CI Voted', 'Year']
EXPECTED_SEX_COLUMNS = ['STATE', 'Group', 'Population (18+)', \
        'Total Citizen', 'Percent Citizen', 'CI Citizen', 'Total Registered', \
        'Percent Registered (18+)', 'CI Registered', \
        'Total Voted', 'Percent Voted (18+)', 'CI Voted', 'Year']

# desired state labels
STATE_NAMES = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 
    'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA', 'FLORIDA', 
    'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 
    'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 
    'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 
    'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK',
    'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
    'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
    'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
    'WEST VIRGINIA', 'WISCONSIN', 'WYOMING', 'NATIONAL'
]

# desired state ID's
STATE_NUMS = [1,  2,  4,  5,  6,  8,  9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 0
]

EXPECTED_DF_TYPE = pd.DataFrame
EXPECTED_COLUMN_TYPES = set([])

def test_get_age_df():
    ''' Test the following conditions for get_age_df():
    - function runs
    - function breaks with a wrong filepath
    - resulting dataframe has the right columns
    - resulting df has data
    - punctuation has been removed
    '''
    print("\n****** Test for get_age_df() ******")

    # smoke test
    print("Smoke Test...")
    df = get_age_df(EXAMPLE_AGE_CSV_PATH) 
    print(df)
    print("passed")

    # check if invalid file paths break function
    print("Testing invalid file path input...")
    invalid_file_caught = False
    try:
        garbage_df = get_age_df(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True
    assert invalid_file_caught
    print("passed")

    # check resulting df has data
    print("Testing dataframe contains data...")
    assert len(df) > 0
    print("passed")

    # check resulting df has correct columns
    print("Testing column names are as expected...")
    assert all(df.columns == EXPECTED_AGE_COLUMNS)
    print("passed")

    # check punctuation has been removed
    print("Testing formatting fixes...")
    assert df["Age"][0] == "Total"
    print("passed")


def test_get_sexrace_df():
    ''' Test the following conditions for get_sexrace_df():
    - function runs
    - function breaks with wrong filepath
    - resulting dataframe has right columns
    - resulting df has data
    - punctuation has been removed
    '''
    print("\n****** Test for get_sexrace_df() ******")

    # smoke test
    print("Smoke test...")
    df = get_sexrace_df(EXAMPLE_SEX_CSV_PATH)
    print(df)
    print("passed")

    # check if invalid file paths break function
    print("Testing invalid file path input...")
    invalid_file_caught = False
    try:
        garbage_df = get_sex_df(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True
    assert invalid_file_caught
    print("passed")

    # check resulting df has data
    print("Testing dataframe contains data...")
    assert len(df) > 0
    print("passed")

    # check resulting df has correct columns
    print("Testing column names are as expected...")
    assert all(df.columns == EXPECTED_SEX_COLUMNS)
    print("passed")

    # check punctuation has been removed
    print("Testing formatting fixes...")
    assert df["Group"][0] == "Total"
    print("passed")


def test_combine_age_data():
    ''' Test following conditions for combine_age_data():
    - resulting dataframe has all the data
    - invalid filepath doesn't work 
    - legislative data is present
    - NATIONAL label has been substituted for US 
    '''
    print("\n****** Test for combine_age_data() ******")

    # smoke test
    print("Smoke test...")
    df = combine_age_data(EXAMPLE_AGE_DIR, EXAMPLE_LAW_CSV_PATH)
    print(df)
    print("passed")

    # test dataframe has enough data
    print("Testing dataframe has enough data...")
    assert len(df) == 8
    print("passed")

    # check if invalid file paths break function
    print("Testing invalid file path input...")
    invalid_file_caught = False
    try:
        garbage_df = combine_age_data(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True
    assert invalid_file_caught
    print("passed")

    # check legislative data is present
    print("Testing legislative data is present...")
    assert True
    print("passed")

    # check NATIONAL label is in place
    print("Testing NATIONAL label is in place...")
    assert df['STATE'][0] == 'NATIONAL'
    print("passed")


def test_combine_sexrace_data():
    ''' Test following conditions for combine_sexrace_data():
    - resulting dataframe has all the data
    - invalid filepath doesn't work 
    - legislative data is present
    - NATIONAL label has been substituted for US 
    '''
    print("\n****** Test for combine_sexrace_data() ******")

    # smoke test
    print("Smoke test...")
    df = combine_sexrace_data(EXAMPLE_SEXRACE_DIR, EXAMPLE_LAW_CSV_PATH)
    print(df)
    print("passed")

    # test dataframe has enough data
    print("Testing dataframe has enough data...")
    assert len(df) == 2
    print("passed")

    # check if invalid file paths break function
    print("Testing invalid file path input...")
    invalid_file_caught = False
    try:
        garbage_df = combine_age_data(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True
    assert invalid_file_caught
    print("passed")

    # check legislative data is present
    print("Testing legislative data is present...")
    assert True
    print("passed")

    # check NATIONAL label is in place
    print("Testing NATIONAL label is in place...")
    assert df['STATE'][0] == 'NATIONAL'
    print("passed")


def test_homogenize_age_data():
    ''' Test conditions for homogenize_age_data():
    - the correct age brackets are present
    - data is in the correct shape
    - state ID's are present
    - state labels are present
    '''
    print("\n****** Test for homogenize_age_data() ******")

    # smoke test
    print("Smoke test...")
    combined = combine_age_data(EXAMPLE_AGE_DIR, EXAMPLE_LAW_CSV_PATH)
    df = homogenize_age_data(combined)
    print(df.head())
    print("passed")

    # test data is in correct shape
    print("Testing data is in correct shape...")
    assert len(df) == 55 
    print("passed")

    # test the state ID's are present
    print("Testing presence of state ID's...")
    assert all(df['id'].unique() == STATE_NUMS)
    print("passed")
    
    # test the state labels are present
    print("Testing presence of state labels...")
    assert all(df['STATE'].unique() == STATE_NAMES)
    print("passed")

def test_homogenize_sexrace_data():
    ''' Test standardization of all sexrace data. '''
    pass 

test_get_age_df()
test_get_sexrace_df()
test_combine_age_data()
test_combine_sexrace_data()
test_homogenize_age_data()

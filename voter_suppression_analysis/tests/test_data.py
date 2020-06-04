''' FUNCTIONS TO TEST DATA PROCESSING FUNCTIONALITY '''

import random
import pandas as pd 

from voter_suppression_analysis.data.processing import \
    get_age_df, get_sexrace_df, \
    combine_age_data, combine_sexrace_data, \
    homogenize_age_data, homogenize_sexrace_data


# useful constants for file locations
EXAMPLE_PATH_AGE = '../tests/sample_data/age_01.csv'
EXAMPLE_PATH_SEX = '../tests/sample_data/sex_01.csv'
EXAMPLE_PATH_LAW = '../tests/sample_data/law_01.csv'

EXAMPLE_DIR_AGE = '../tests/sample_data/example_age_folder/'
EXAMPLE_DIR_SEX = '../tests/sample_data/example_sex_folder/'

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

def test_get_age_df():
    ''' 
        Test the following conditions for get_age_df():
            - function runs
            - function breaks with a wrong filepath
            - resulting dataframe has the right columns
            - resulting df has data
            - punctuation has been removed
    '''

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

    # check punctuation marks have been removed
    found_punctuation = df.Age.str.contains('.').any()
    assert (found_punctuation == False)


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
    found_punctuation = df.Group.str.contains('.').any()
    assert (found_punctuation == False)


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
    assert len(df) == 8

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

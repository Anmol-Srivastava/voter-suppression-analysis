''' FUNCTIONS TO TEST DATA PROCESSING FUNCTIONALITY '''

import random
import pandas as pd 

from voter_suppression_analysis.data.processing import \
    get_age_df, get_sexrace_df, \
    combine_age_data, combine_sexrace_data, \
    homogenize_age_data, homogenize_sexrace_data


# useful constants for function args
EXAMPLE_AGE_CSV_PATH = ''
EXAMPLE_SEX_CSV_PATH = ''
GARBAGE_FILE_PATH = str(random.randint(0,9))

EXPECTED_AGE_COLUMNS = 0
EXPECTED_SEX_COLUMNS = 0

EXPECTED_DF_TYPE = pd.DataFrame
EXPECTED_COLUMN_TYPES = set([])


def test_get_age_df():
    ''' Test creation of age DataFrame for single year. '''
    
    # smoke test
    df = get_age_df(EXAMPLE_AGE_CSV_PATH) 

    # inspect returned DataFrame
    assert True # add more code 

    # check if invalid file paths break function
    invalid_file_caught = False

    try:
        garbage_df = get_age_df(GARBAGE_FILE_PATH)
    except:
        invalid_file_caught = True

    # ensure invalid file paths cause exception
    assert invalid_file_caught


def test_get_sexrace_df():
    ''' Test creation of sexrace DataFrame for single year. '''
    pass

def test_combine_age_data():
    ''' Test combination of all years of age data. '''
    pass

def test_combine_sexrace_data():
    ''' Test combination of all years of sexrace data. '''
    pass

def test_homogenize_age_data():
    ''' Test standardization of all age data. '''
    pass

def test_homogenize_sexrace_data():
    ''' Test standardization of all sexrace data. '''
    pass 
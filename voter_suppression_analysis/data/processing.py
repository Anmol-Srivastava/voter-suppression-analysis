'''
Code to load, clean, and combine all relevant data.
See README for references re: data.
'''
import glob
import pandas as pd


#############
# CONSTANTS #
#############


# useful constants for accessing files
AGE_PATH_REGEX = 'clean/*_age.csv'
SEX_PATH_REGEX = 'clean/*_sexrace.csv'
LAWS_DATA_PATH = 'clean/suppression.csv'

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

KEEP_AGE_COLUMNS = [
    'state', 'age_bracket', 'total', 'total_reg', 'total_voted',
    'percent_reg', 'percent_voted', 'yr'
]

KEEP_SEX_COLUMNS = ['state', 'group', 'percent_reg', 'percent_voted', 'yr']

# useful constants for standardizing state labels
STATE_NAMES = ['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA',
    'COLORADO', 'CONNECTICUT', 'DELAWARE', 'DISTRICT OF COLUMBIA', 'FLORIDA',
    'GEORGIA', 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 
    'KENTUCKY', 'LOUISIANA', 'MAINE', 'MARYLAND', 'MASSACHUSETTS', 
    'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 
    'NEVADA', 'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK',
    'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
    'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
    'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
    'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'
]

# note these integers are related to US Census Bureau ordering
STATE_NUMS = [1,  2,  4,  5,  6,  8,  9, 10, 11, 12, 13, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56,
]

STATES_TABLE = zip(STATE_NAMES, STATE_NUMS)


#############
# FUNCTIONS #
#############


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
    df.state = df.state.str.upper()
    df.yr = df.yr.astype(str)
    df.total = df.total.apply(pd.to_numeric, errors='coerce')
    df.total_reg = df.total_reg.apply(pd.to_numeric, errors='coerce')
    df.total_reg = df.total_reg.apply(pd.to_numeric, errors='coerce')
    df.age_bracket = df.age_bracket.map(lambda x: x.lstrip('.'))
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
    df.state = df.state.str.upper()
    df.yr = df.yr.astype(str)
    df.percent_reg = df.percent_reg.apply(pd.to_numeric, errors='coerce')
    return df


def combine_age_data():
    '''
    Retrieve all age-related data files, combine into one pd.DataFrame
    object, and attach legislative data columns.

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

    # concatenate and attach legislative data
    combined = pd.concat(df_list, axis=0, ignore_index=True)
    laws_df = pd.read_csv(LAWS_DATA_PATH)
    laws_df.state = laws_df.state.str.upper()

    result_df = combined.merge(laws_df,
                               how='outer',
                               left_on='state',
                               right_on='state')

    # make nationwide labels consistent and finish
    result_df.state.loc[result_df.state == 'US'] = 'NATIONAL'
    result_df.state.loc[result_df.state == 'UNITED STATES'] = 'NATIONAL'
    return result_df


def combine_sexrace_data():
    '''
    Retrieve all sexrace-related data files, combine into one
    pd.DataFrame object, and attach legislative data columns.

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

    # concatenate and attach legislative data
    combined = pd.concat(df_list, axis=0, ignore_index=True)
    laws_df = pd.read_csv(LAWS_DATA_PATH)
    laws_df.state = laws_df.state.str.upper()

    result_df = combined.merge(laws_df,
                               how='outer',
                               left_on='state',
                               right_on='state')

    # make nationwide labels consistent and finish
    result_df.state.loc[result_df.state == 'US'] = 'NATIONAL'
    result_df.state.loc[result_df.state == 'UNITED STATES'] = 'NATIONAL'
    return result_df


def homogenize_age_data(df):
    """
    Structures the age data by creating the desired age groups
    of 'Total','18 to 44', '45 to 65', '65+' into a DataFrame.

    Args:
        df_in: Dataframe created by function combine_age_data()

    Returns:
        pd.DataFrame, age bracket structured data for all years
    """
    df_states = pd.DataFrame(STATES_TABLE, columns=['state', 'id'])
    df_states.state = df_states.state.str.capitalize()

    # splitting inconsistent age brackets into many DFs
    df_65plus = df.loc[(df.age_bracket == '65 to 74')
        | (df.age_bracket == '75+')
        | (df.age_bracket == '65 to 75')
        | (df.age_bracket == '65+'),
    ]

    df_45_64 = df.loc[(df.age_bracket == '45 to 64')
        | (df.age_bracket == '45 to 55')
        | (df.age_bracket == '55 to 65')
        | (df.age_bracket == '45 to 65'),
    ]

    df_18_44 = df.loc[(df.age_bracket == '18 to 24')
        | (df.age_bracket == '18 to 25')
        | (df.age_bracket == '25 to 44')
        | (df.age_bracket == '25 to 35')
        | (df.age_bracket == '35 to 45')
        | (df.age_bracket == '25 to 45')
        | (df.age_bracket == '25 to 34')
        | (df.age_bracket == '35 to 44'),
    ]

    df_total = df.loc[df.age_bracket == 'Total',]

    # iteratively group these DFs by state and year
    df_list = [df_total, df_18_44, df_45_64, df_65plus]
    age_brackets = ['Total','18 to 44', '45 to 65', '65+']
    result = []

    for i, df in enumerate(df_list):
        df = df.groupby(['state', 'yr'], sort=False).sum().reset_index()
        df['age_bracket'] = age_brackets[i]
        result.append(df)

    # recombine all age bracket DFs
    result = pd.concat(result, axis=0, ignore_index=True)
    result.sort_values(['yr', 'state'], inplace=True)

    # compute voter turnout metric
    result['percent_reg'] = result.total_reg / result.total
    result['percent_voted'] = result.total_voted / result.total

    # refomatting
    result.yr = result.yr.astype(int)
    result.state = result.state.str.capitalize()

    # attach our state labels/IDs and finish
    result = pd.merge(result, df_states, left_on='state', right_on='state')
    return result


def homogenize_sexrace_data(df):
    raise NotImplemented

'''
Code to load, clean, and combine all relevant data.
See README for references re: data.
'''
import glob
import pandas as pd


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

KEEP_AGE_COLUMNS = ['state', 'age_bracket', 'total', 'total_reg', 'total_voted', 'percent_reg', 'percent_voted', 'yr']
KEEP_SEX_COLUMNS = ['state', 'group', 'percent_reg', 'percent_voted', 'yr']


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
    result_df.state.loc[result_df.state == 'US'] = 'NATIONAL'
    result_df.state.loc[result_df.state == 'UNITED STATES'] = 'NATIONAL'
    return result_df

def setup_age_dataframe(df_in):
    """
    Structures the age data by creating the desired age groups
    of 'Total','18 to 44', '45 to 65', '65+' into a DataFrame.

    Args:
        df_in: Dataframe created by function combine_age_data()

    Returns:
        pd.DataFrame, age bracket structured data for all years
    """

    # Setting ID numbers to match US Census for each state
    STATEID=[['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS',
        'CALIFORNIA', 'COLORADO', 'CONNECTICUT', 'DELAWARE',
        'DISTRICT OF COLUMBIA', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO',
        'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
        'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
        'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA',
        'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK',
        'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
        'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
        'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON',
        'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'],
             [1,  2,  4,  5,  6,  8,  9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20,
              21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
              38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56,]]
    idState = pd.DataFrame(STATEID).T
    idState.columns = ['state','id']
    idState.state = idState.state.str.capitalize()

    # creating individual age bracket dataframes
    df65plus = df_in.loc[(df_in.age_bracket == '65 to 74') | (df_in.age_bracket == '75+') |
                         (df_in.age_bracket == '65 to 75') | (df_in.age_bracket == '65+'),]
    df4564plus = df_in.loc[(df_in.age_bracket == '45 to 64') | (df_in.age_bracket == '45 to 55') |
                           (df_in.age_bracket == '55 to 65') | (df_in.age_bracket == '45 to 65'),]
    df1844plus = df_in.loc[(df_in.age_bracket == '18 to 24') | (df_in.age_bracket == '18 to 25')| 
                           (df_in.age_bracket == '25 to 44') | (df_in.age_bracket == '25 to 35') | 
                           (df_in.age_bracket == '35 to 45') | (df_in.age_bracket == '25 to 45') |
                           (df_in.age_bracket == '25 to 34') | (df_in.age_bracket == '35 to 44'),]
    dftotal = df_in.loc[df_in.age_bracket == 'Total',]

    # setting values and parameters to be fed into for loop
    dfs_age = [dftotal, df1844plus, df4564plus, df65plus]
    age_bracket = ['Total','18 to 44', '45 to 65', '65+']
    dfages = []
    for i, df in enumerate(dfs_age):
        df = df.groupby(['state', 'yr'], sort=False).sum().reset_index()
        df['age_bracket'] = age_bracket[i]
        dfages.append(df)

    dfages = pd.concat(dfages, axis=0, ignore_index=True)
    dfages.sort_values(['yr','state'], inplace=True)

    # calculating the Percentage value of voter turnout
    dfages['percent_reg'] = dfages.total_reg / dfages.total
    dfages['percent_voted'] = dfages.total_voted / dfages.total
    dfages.yr = dfages.yr.astype(int)
    dfages.state = dfages.state.str.capitalize()

    # adding the ID number to the states
    df_out = pd.merge(dfages, idState, left_on='state', right_on='state')

    return df_out

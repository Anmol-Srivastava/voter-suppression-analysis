import pandas as pd
import glob

#############
# CONSTANTS #
#############

# filepath expressions for data
AGE_FILES = 'clean/*_age.csv'
SEXRACE_FILES = 'clean/*_sexrace.csv'
LAWS_DATA_PATH = 'clean/supression.csv'

# useful constants for renaming and removing columns
'''AGE_COLUMN_NAMES = [
    'state', 'age_bracket', 'total', 'total_reg', 'percent_reg',
    'ci_reg', 'total_voted', 'percent_voted', 'ci_voted', 'yr'
]'''

SEX_COLUMN_NAMES = [
    'STATE', 'Group', 'Population (18+)', 'Total Citizen', 'Percent Citizen', 'CI Citizen',
    'Total Registered', 'Percent Registered (18+)', 'CI Registered', 'Total Voted', 'Percent Voted (18+)',
    'CI Voted', 'Year'
]

# desired columns to subset from data
KEEP_AGE_COLUMNS = [
    'STATE', 'Age', 'Total', 'Total Registered', 'Percent registered (18+)',
    'CI Registered', 'Total Voted', 'Percent voted (18+)', 'CI Voted', 'Year'
]

KEEP_SEX_COLUMNS = [
    'STATE', 'Group', 'Population (18+)', 'Total Citizen', 'Percent Citizen', 'CI Citizen',
    'Total Registered', 'Percent Registered (18+)', 'CI Registered', 'Total Voted', 'Percent Voted (18+)',
    'CI Voted', 'Year'
]

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

# note these integers are related to US Census Bureau ordering
STATE_NUMS = [1,  2,  4,  5,  6,  8,  9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
    38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 0
]

STATES_TABLE = list(zip(STATE_NAMES, STATE_NUMS))


#############
# FUNCTIONS #
#############


def get_age_df(file_path):
    '''
    Load age data by file name into pd.DataFrame and
    return DataFrame object with select columns and cleaned
    values.

    Note: NaN values are kept for possible use in modeling/viz.

    Args:
        file_path: str, designating file to retrieve for a given year

    Returns:
        pd.DataFrame, processed age data for that year
    '''

    # load and subset data
    df = pd.read_csv(file_path, header=0)
    df = df[KEEP_AGE_COLUMNS]

    # clean up format and unwanted punctuation
    df["STATE"] = df["STATE"].str.upper()
    df["Year"] = df["Year"].astype(str)
    df['Total'] = df['Total'].replace(',','', regex=True).apply(pd.to_numeric, errors='coerce')
    df['Total Registered'] = df['Total Registered'].replace(',','', regex=True).apply(pd.to_numeric, errors='coerce')
    df['Total Voted'] = df['Total Voted'].replace(',','', regex=True).apply(pd.to_numeric, errors='coerce')
    df['Age'] = df['Age'].map(lambda x: x.lstrip('.'))

    return df


def get_sexrace_df(file_path):
    '''
    Load sexrace data by file name into pd.DataFrame
    and return DataFrame object with select columns and cleaned
    values.

    Note: NaN values are kept for possible use in modeling/viz.

    Args:
        file_path: str, file for which to retrieve sexrace data

    Returns:
        pd.DataFrame, processed sexrace data for that year
    '''

    # load and subset data
    df = pd.read_csv(file_path, header=0, names=SEX_COLUMN_NAMES)
    df = df[KEEP_SEX_COLUMNS]

    # clean up format and unwanted punctuation
    df["STATE"] = df["STATE"].str.upper()
    df["Year"] = df["Year"].astype(str)
    df["Total Citizen"] = df["Total Citizen"].replace(',','', regex=True).apply(pd.to_numeric, errors='coerce')
    df["Total Registered"] = df["Total Registered"].replace(',','', regex=True).apply(pd.to_numeric, errors='coerce')
    df["Total Voted"] = df["Total Voted"].replace(',','', regex=True).apply(pd.to_numeric, errors='coerce')
    df["Group"] = df["Group"].map(lambda x: x.lstrip('.'))

    return df


def combine_age_data(file_expression=AGE_FILES, law_filepath=LAWS_DATA_PATH):
    '''
    Generate all age-related dataframes, combine into one,
    and attach legislative data columns.

    Args:
        file_expression: str, regex to capture desired age files
        law_filepath: str, filepath to legislation data

    Returns:
        pd.DataFrame, combined age data for all years
    '''

    # retrieve all relevant file paths
    age_file_paths = glob.glob(file_expression)
    df_list = []

    # generate a dataframe from each file and combine
    for age_file in age_file_paths:
        print('Reading %s...' % age_file)
        df = get_age_df(age_file)
        df_list.append(df)
    
    combined = pd.concat(df_list, axis=0, ignore_index=True)

    # load legislative data
    laws_df = pd.read_csv(law_filepath)
    laws_df["STATE"] = laws_df["STATE"].str.upper()

    # make nationwide labels consistent
    combined["STATE"].loc[combined["STATE"] == 'US'] = 'NATIONAL'
    combined["STATE"].loc[combined["STATE"] == 'UNITED STATES'] = 'NATIONAL'
    laws_df["STATE"].loc[laws_df["STATE"] == 'US'] = 'NATIONAL'

    # attach legislative rating to age data
    result_df = combined.merge(laws_df,
                               how='outer',
                               left_on='STATE',
                               right_on='STATE')

    return result_df


def combine_sexrace_data(file_expression=SEXRACE_FILES, law_filepath=LAWS_DATA_PATH):
    '''
    Retrieve all sexrace-related data files, combine into one
    pd.DataFrame object, and attach legislative data columns.

    Args:
        file_expression: str, regex to capture desired age files
        law_filepath: str, filepath to legislation data

    Returns:
        pd.DataFrame, combined sexrace data for all years
    '''

    # retrieve all relevant file paths
    sex_file_paths = glob.glob(file_expression)
    df_list = []

    # generate a dataframe from each file and combine
    for sex_file in sex_file_paths:
        print('Reading %s...' % sex_file)
        df = get_sexrace_df(sex_file)
        df_list.append(df)
    combined = pd.concat(df_list, axis=0, ignore_index=True)

    # load legislative data
    laws_df = pd.read_csv(law_filepath)
    laws_df["STATE"] = laws_df["STATE"].str.upper()

    # make nationwide labels consistent
    combined["STATE"].loc[combined["STATE"] == 'US'] = 'NATIONAL'
    combined["STATE"].loc[combined["STATE"] == 'UNITED STATES'] = 'NATIONAL'
    laws_df["STATE"].loc[laws_df["STATE"] == 'US'] = 'NATIONAL'

    # attach legislative rating to sex/race data
    result_df = combined.merge(laws_df,
                               how='outer',
                               left_on='STATE',
                               right_on='STATE')

    return result_df


def homogenize_age_data(df):
    """
    Structures the age data by creating the desired age groups
    of 'Total','18 to 44', '45 to 65', '65+' into a DataFrame.

    Args:
        df: Dataframe created by function combine_age_data()

    Returns:
        pd.DataFrame, age bracket structured data for all years
    """
    # set up a table for the states
    df_states = pd.DataFrame(STATES_TABLE, columns=['STATE', 'id'])
    df_states["STATE"] = df_states["STATE"].str.upper()

    # combine existing age brackets for uniformity
    df_65plus = df.loc[(df["Age"] == '65 to 74')
        | (df["Age"] == '75+')
        | (df["Age"] == '65 to 75')
        | (df["Age"] == '65+'),
    ]
    df_45_64 = df.loc[(df["Age"] == '45 to 64')
        | (df["Age"] == '45 to 55')
        | (df["Age"] == '55 to 65')
        | (df["Age"] == '45 to 65'),
    ]
    df_18_44 = df.loc[(df["Age"] == '18 to 24')
        | (df["Age"] == '18 to 25')
        | (df["Age"] == '25 to 44')
        | (df["Age"] == '25 to 35')
        | (df["Age"] == '35 to 45')
        | (df["Age"] == '25 to 45')
        | (df["Age"] == '25 to 34')
        | (df["Age"] == '35 to 44'),
    ]
    df_total = df.loc[df["Age"] == 'Total',]

    # iteratively group these DFs by state and year
    df_list = [df_total, df_18_44, df_45_64, df_65plus]
    age_brackets = ['Total','18 to 44', '45 to 65', '65+']
    combined = []

    for i, df in enumerate(df_list):
        df = df.groupby(['STATE', 'Year'], sort=False).sum().reset_index()
        df['Age'] = age_brackets[i]
        combined.append(df)

    # recombine all age bracket DFs
    result = pd.concat(combined, axis=0, ignore_index=True)
    result.sort_values(['Year', 'STATE'], inplace=True)

    # compute voter turnout metric
    result['Percent Registered'] = result['Total Registered'] / result['Total']
    result['Percent Voted'] = result['Total Voted'] / result['Total']

    # refomatting
    result['Year'] = result['Year'].astype(int)
    result['STATE'] = result['STATE'].str.upper()
    result = result.rename(columns={'Age':'Group'})

    # attach our state labels/IDs
    result = df_states.merge(result, how='outer', left_on='STATE', right_on='STATE')
    return result

def homogenize_sexrace_data(df_in):
    """
    Structures the age data by creating the desired demographic groups
    of 'Total','Male', 'Female', 'White', 'Black', 'Asian & Pacific Islander',
    'Hispanic' into a DataFrame.

    Args:
        df_in: Dataframe created by function combine_age_data()

    Returns:
        pd.DataFrame, age bracket structured data for all years
    """
    df_states = pd.DataFrame(STATES_TABLE, columns=['STATE', 'id'])
    df_states.STATE = df_states.STATE.str.upper()

    # useful constants for renaming relevant demographic groups
    ORIGINAL_GROUPS = ['Total', 'Male', 'Female', 'N-H White','N-H Black',
                       'API', 'Hispanic', 'Non-Hispanic White', 'Non-Hispanic Black',
                       'Asian and Pacific Islander','White non-Hispanic alone',
                       'Black alone', 'Asian alone','Hispanic (of any race)']
    RENAME_GROUPS = ['Total', 'Male', 'Female', 'White', 'Black',
                     'Asian & Pacific Islander','Hispanic', 'White',
                     'Black', 'Asian & Pacific Islander','White','Black',
                     'Asian & Pacific Islander','Hispanic']

    # useful constants for the 'total's columns to work with
    TOTALS_COLUMNS = ['Total Citizen', 'Total Registered', 'Total Voted']

    # interatively renaming demographic groups
    df = df_in.copy()
    for (og, rm) in zip(ORIGINAL_GROUPS, RENAME_GROUPS):
        df.Group.loc[df.Group == og] = rm

    # keeping relevant groups and setting years as str
    df_groups_kept = df.loc[df.Group.isin(RENAME_GROUPS)]
    df_groups_kept.Year = df_groups_kept.Year.astype(float).astype(int).astype(str)

    # interatively validating the 'total's values
    for col in TOTALS_COLUMNS:
        df_temp = df_groups_kept.pivot_table(index=['STATE','Year','restrictive_id_laws','felony_disenfranchisement'],
                                             columns='Group', values=col)
        df_temp = df_temp.reset_index()
        if (('Male' in df_temp.columns) & ('Female' in df_temp.columns)):
            totals = df_temp[['Male', 'Female']].sum(axis=1)
            df_temp.Total = totals
        df_temp_unpivot = df_temp.melt(id_vars=['STATE','Year','restrictive_id_laws','felony_disenfranchisement'],
                                       value_name=col)
        if col == 'Total Citizen':
            df_merge = df_temp_unpivot.copy()
        else:
            next
        df_merge = pd.merge(df_merge, df_temp_unpivot, how='left',
                           left_on=['STATE', 'Year', 'Group','restrictive_id_laws','felony_disenfranchisement'],
                            right_on=['STATE', 'Year', 'Group','restrictive_id_laws','felony_disenfranchisement'])
    # reformating values and column names
    df_merge_kept = df_merge.drop('Total Citizen_y', axis=1)
    df_merge_kept.STATE = df_merge_kept.STATE.str.upper()
    df_demo_out = df_merge_kept.rename(columns={"Total Citizen_x":'Total'})
    df_demo_out = df_demo_out.sort_values(by=['Year', 'STATE']).round()
    df_demo_out.Year = df_demo_out.Year.astype(int)

    # calculating the percentage of voter turnout totals
    df_demo_out['Percent Registered'] = df_demo_out['Total Registered'] / df_demo_out['Total']
    df_demo_out['Percent Voted'] = df_demo_out['Total Voted'] / df_demo_out['Total']

    # attach our state labels/IDs and finish
    df_demo_out = pd.merge(df_demo_out, df_states, left_on='STATE', right_on='STATE')

    return df_demo_out

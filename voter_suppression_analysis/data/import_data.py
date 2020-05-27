'''
Import available data into pandas dataframes
'''
import glob
import pandas as pd

def read_data(folder_path):
    '''
    Read all the data files in a folder and combine them into
    one pandas dataframe
    Input:
      folder_path - path to folder containing separate csv files
    Output:
      combined - a pandas dataframe with all data concatenated
    '''
    path = folder_path
    age_files = glob.glob(path + "/*.csv")
    df_list = []

    for filename in age_files:
        print("Reading %s" %filename)
        data = pd.read_csv(filename, index_col=None, header=0)
        df_list.append(data)

    combined = pd.concat(df_list, axis=0, ignore_index=True)
    print("\nCombined Data:\n")
    print(combined)
    return combined

read_data('raw/age')
read_data('raw/sexrace')

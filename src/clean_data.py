import os
import pandas as pd


def data_gather(dir_string):
    '''
    Gather csv files that have been saved in data folder below project
    working directory and combine in one dataframe.

    ARG: string value of the data directory name
    OUTPUT: Pandas dataframe containing contents of all files from input directory
    '''
    all_files = [f for f in os.listdir(dir_string) if f.endswith('csv')]

    li = []

    for filename in all_files:
        df = pd.read_csv(dir_string + filename, index_col=None, header=0)
        li.append(df)

    all5yrsdf = pd.concat(li, axis=0, ignore_index=True)
    return all5yrsdf


def clean_header_row(df):
    '''
    Remove undesirable chars and replace column names in df from
    original download for cleaner workflow

    ARG: Pandas df
    OUTPUT: Pandas df
    '''
    
    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_'
                ).str.replace('(', '').str.replace(')', '')
    
    df = df.rename(columns={'date/time_pst': 'dt_time_pst',
                            'relative_humidity_%':'rel_humidity_percent',
                            'precipitation_"': 'precip',
                            'total_snow_depth_"': 'total_snow_depth',
                            '24_hour_snow_"': '24_hr_snow'})

    return df

def sort_date_time(df):
    '''
    Sort all of the data rows by timestamp in case files were not loaded into initial df 
    chronologically, and convert the timestamp column to a standard date time object that 
    can be used for more functionality.

    ARG: Pandas df
    OUTPUT: Pandas df
    '''
    
    df_sorted = df.sort_values('dt_time_pst')
    df_dtdf = df_sorted.copy()
    df_dtdf['dt_time_pst'] = pd.to_datetime(df_sorted['dt_time_pst'])

    return df_dtdf

def drop_col(df, col):
    '''
    Make df more concise by droppig unnecessary columns, such as 'battery_voltage_v'.

    ARG: df  - Pandas df
        col  - Name of column in string
    OUTPUT: Pandas df
    '''
    df.drop(col, axis=1, inplace=True)
    return df

def month_df(df, month_number):
    '''
    Create subset df for specific month

    ARGS: Pandas df 
          month_number - int between 1-12
    OUTPUT: Pandas df
    '''

    month_df = df[(df['dt_time_pst'].dt.month == month_number)]
    return month_df

def add_precip_cols(monthdf):
    '''
    Add columns to differentiate different types of precipitation.

    ARG: df  - Pandas df
    OUTPUT: Pandas df
    '''
    
    df = monthdf.copy()
    rainmask = df['temperature_deg_f'] > 32
    snowmask = df['temperature_deg_f'] <= 32
    df['hrly_rain'] = df['precip'][rainmask]
    df['hrly_snow'] = df['precip'][snowmask]

    df['hrly_rain'] = df['hrly_rain'].fillna(0)
    df['hrly_snow'] = df['hrly_snow'].fillna(0)

    return df

    

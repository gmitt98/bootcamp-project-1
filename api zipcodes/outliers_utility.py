def single_year_outliers(year):

    import pandas as pd
    import numpy as np

    # Read in outlier zipcode data
    file_path_zips = "../data/analysis/annual_outlier_zips.csv"
    annual_outlier_zips_df = pd.read_csv(file_path_zips)
    annual_outlier_zips_df.drop(columns=annual_outlier_zips_df.columns[0], axis=1, inplace=True)

    file_path_values = "../data/analysis/annual_outlier_values.csv"
    annual_outlier_values_df = pd.read_csv(file_path_values)
    annual_outlier_values_df.drop(columns=annual_outlier_values_df.columns[0], axis=1, inplace=True)

    # Create a dataframe with zip codes for the year you want
    year_zips_df = pd.DataFrame()
    year_zips = annual_outlier_zips_df[year]
    year_zips_df[year] = year_zips

    # Create a dataframe with values for the year  you want
    year_values_df = pd.DataFrame()
    year_values = annual_outlier_values_df[year]
    year_values_df[year] = year_values

    # Remove empty cells to leave only the year you want
    year_zips_cleaned_df = year_zips_df.dropna().copy()
    year_values_cleaned_df = year_values_df.dropna().copy()

    # Rename the columns
    year_zips_cleaned_df.rename(columns={year: "zip_code"}, inplace=True)
    year_values_cleaned_df.rename(columns={year: "Annual Change (%)"}, inplace=True)

    # Merge the two cleaned DataFrams
    merge_df = year_zips_cleaned_df.join(year_values_cleaned_df)
    
    # Pass this out of the function for use in larger code
    return merge_df
    
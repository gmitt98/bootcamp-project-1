### Project 1: Craig, Mary O., Sydney, Galen

## Analysis Overview
This project looks at house prices in the US over time, and how various factors influence them.
We have some national overviews as well as local and regional analysis.

# Objective:
Investigating the impact of interest rates, recession, and proximity to services (such as schools and parks) on the housing market, broken down roughly by Zip Code: use the Federal Reserve's interest rate data and home price data from sources like Zillow, Redfin, and the Fed's Case-Shiller home price index to study how changes in interest rates affect the housing market.  See the Analysis Plan file for more detail.

# Workflow:
Four analysts shared the work.  The four areas of work, roughly in order the work was done, were:
1. Data collection using APIs and data cleaning (this analyst also did analysis on recessions and modeling)
2. Determining national growth and decline outliers by Zip Code over various time periods, with some interpretation of the resulting maps
3. Data collection of Zip Code coordinates (for mapping), and counting of proximal schools and parks, using Geoapify
4. Data visualizations including all plots and maps

Collaborative work was managed on GitHub.  Analysts 1-3 largely worked with individual Notebooks, passing data and results to one another through .csv files stored in the repo.  Analyst 4 added plotting and mapping into the analysis Notebooks and saved images for presentation.


## Understanding this Repo
The content in this folder is as follows:
 * data folder: contains the raw downloaded data from various sources
   ** cleaned data sub-folder: contains the cleaned data files that we use in our analyses
   ** analysis sub-folder: outputs of analyses
* api_zipcodes folder: contains the notebooks and python code used to do the API calls for various mapping and finding points of interest around our ZIP codes
* Presentation folder: contains the inital project introduction, and then our final project presentation slides
* Visuals folder: contains the charts and graphs and maps that we generated in our analyses
* jupyter notebook files: these live in the top level of this repo, and they are the notebook used for the various analysis. Note: we kept to 1 notebook per use case: data cleaning, data merging, research question analysis... we contain these for ease of collaboration and version control.

Notebook annual_outliers_py.ipynb in the tip directory opens cleaned hpi data from /data/cleaned data/cleaned_hpi_price_data.csv and determines outliers for each year based on the difference from the prior year, for all 13,000 unique zip codes for 48 years from 1975 to 2022.  It saves the output to .csv files in data/analysis.

Notebook period_outliers_difference_py.ipynb in the top directory opens cleaned hpi data from /data/cleaned data/cleaned_hpi_price_data.csv and determines outliers based on the difference from the earlier year for each period of 3, 5, 10, 20, and 48 years, for all 13,000 unique zip codes for 48 years from 1975 to 2022.  It saves the results to .csv files in /data/analysis.

Notebook period_outliers_ratio_py.ipynb in the top directory opens cleaned hpi data from /data/cleaned data/cleaned_hpi_price_data.csv and determines outliers based on the percent change from the earlier year for each period of 3, 5, 10, 20, and 48 years, for all 13,000 unique zip codes for 48 years from 1975 to 2022.  It saves the results to .csv files in /data/analysis.

Notebook zip_coordinates.ipynb in the /api_zipcodes directory takes a list of zip_codes from a .csv file whose path is typed directly into the code, and adds columns for latitude and longitude to the dataframe and resaves it as a new .csv file in /data/analysis.

Python file outliers_utility.py in the /api_zipcodes directory is a script that defines a function to open the two annual_outliers .csv files in /data/analysis and merge the results into a single dataframe for a single year, to make further analysis more convenient.  This could be called in a loop.

Python script zip_coordinates_function.py in the /api_zipcodes directory is a script that defines a function to enter a single zip code and return its latitude and longitude as variables.  This was used in a loop in zip_coordinates.ipynb notebook in the same directory to loop through lists of zip codes and return their coordinates for mapping.

## Files not on Git
 * Large datafiles: original Redfin data, saved raw cleaned data
 * API keys

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

## Files not on Git
 * Large datafiles: original Redfin data, saved raw cleaned data
 * API keys

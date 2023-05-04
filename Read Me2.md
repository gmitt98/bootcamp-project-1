# Objective:
Investigating the impact of interest rates, recession, and proximity to services (such as schools and parks) on the housing market, broken down roughly by Zip Code: use the Federal Reserve's interest rate data and home price data from sources like Zillow, Redfin, and the Fed's Case-Shiller home price index to study how changes in interest rates affect the housing market.  See the Analysis Plan file for more detail.

# Workflow:
Four analysts shared the work.  The four areas of work, roughly in order the work was done, were:
1 - Data collection using APIs and data cleaning (this analyst also did analysis on recessions and modeling)
2 - Determining national growth and decline outliers by Zip Code over various time periods, with some interpretation of the resulting maps
3 - Data collection of Zip Code coordinates (for mapping), and counting of proximal schools and parks, using Geoapify
4 - Data visualizations including all plots and maps

Collaborative work was managed on GitHub.  Analysts 1-3 largely worked with individual Notebooks, passing data and results to one another through .csv files stored in the repo.  Analyst 4 added plotting and mapping into the analysis Notebooks and saved images for presentation.

# Repo Structure:
The top directory has Notebooks and files for Analysts 1 and 2, as well as documents (slides) for presentation.  Collected data from Analyst 1 were stored in the /data directory - the resulting cleaned data was stored in /data/cleaned data.  Analyst 2 stored results in /data/analysis.  Analyst 3 has Notebooks and results in directory /api_zipcodes.  Analyst 4 stored plots and maps in the /Visuals directory.

The group's analysis comments are found in the presentation materials in the top directory.
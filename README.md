# 311 Call Data

This project takes a look at all 311 calls made in the city of Louisville in 2016, groups them by month, and looks for a correlation between call volume and the month of the year.

## Getting Started

1. Clone the Github repository to your computer
2. Run the load_data.py file.  This will set up the database and load the csv file into the database.  The csv is included in the repository, but was sourced from Louisville Metro Open Data: https://data.louisvilleky.gov/dataset/311-service-requests/resource/e3879b84-c881-413a-814c-07a2042131d6#{view-graph:{graphOptions:{hooks:{processOffset:{},bindEvents:{}}}},graphOptions:{hooks:{processOffset:{},bindEvents:{}}},view-map:{lonField:!longitude,latField:!latitude}}
3. Open the Jupyter Notebook file 311_calls.ipynb and run the cell.  This will do a number of things:
    - Creates a new table named 'months' and inserts the month as an integer from the requested_datetime column in the original table data_311
    - Selects the data from the 'months' table
    - Fetches the data in a dataframe named 'dat'
    - Renames the column header of the dataframe to 'months'
    - Groups the month integers together, counts the total amount of occurances of each month and saves the data into the variable dat_agg
    - Using Matplotlib, plots the total number of 311 calls received for each month of the year 2016
    - Commits the changes and closes the database connection
    
## Conclusion

From looking at the data in the plot, it appears that there is a large increase in 311 call volume during the warmer months of the year.  Call volume is near or over 9000 calls per month for each month from March through September and close to or under 5000 calls per month from October through February.
    
  

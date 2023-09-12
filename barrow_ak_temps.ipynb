
# Earth Data Science Coding Challenge!

import hvplot.pandas
import pandas as pd

# Define the URL for Barrow mean temperature data download
barrow_temp_url = (
    'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-'
    'glance/city/time-series/USW00027502/tmax/12/7/1895-2023.csv')
barrow_temp_url

# List all current variables
%whos

# Import Barrow temperature values from NCEI
barrow_temp_df = pd.read_csv(
    barrow_temp_url, header=3, names=['year', 'temperature_f'])
barrow_temp_df

# Extract the year from the data
barrow_temp_df.year = pd.to_datetime(barrow_temp_df.year, format='%Y%m').dt.year

barrow_temp_df

# Compute temperatures in Celcius
barrow_temp_df['temperature_c'] = (barrow_temp_df['temperature_f'] - 32) * 5 / 9

barrow_temp_df

# Plot the Barrow Temperature data over time
barrow_temp_df.hvplot(
    x='year', y='temperature_f',
    title='Mean Annual Temperature in Barrow, AK, USA',
    xlabel='Year', ylabel='Temperature (°F)')

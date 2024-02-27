import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

df = pd.read_csv('Activities\SeaLevelPredictor\epa-sea-level.csv', header=0)
# Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
plt.show()

# Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
future_year = 2050
predicted_sea_level = slope * future_year + intercept
plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label=f'Line of Best Fit\nPredicted Sea Level in 2050: {predicted_sea_level:.2f} inches')
plt.scatter(x=future_year, y=predicted_sea_level, color='green', marker='*', s=200, label=f'Predicted Sea Level in 2050: {predicted_sea_level:.2f} inches')
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level')
plt.title('Sea Level Rise Over Years')
plt.legend()

plt.show()


# Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
df_recent = df[df['Year'] >= 2000]

# Create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', label='Original Data')
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
future_years = np.arange(2000, 2051)
predicted_sea_levels = slope_recent * future_years + intercept_recent
plt.plot(future_years, predicted_sea_levels, color='red', label='Line of Best Fit')
plt.scatter(x=2050, y=predicted_sea_levels[-1], color='green', marker='*', s=200, label=f'Predicted Sea Level in 2050: {predicted_sea_levels[-1]:.2f} inches')
# The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.show()
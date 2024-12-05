import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    

    # Create first line of best fit
    year_extended = df['Year']._append(pd.Series(range(2014, 2051)),ignore_index=True)
    lin_regress_result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    lin_regress_line_y = lin_regress_result.slope*year_extended+lin_regress_result.intercept
    plt.plot(year_extended, lin_regress_line_y, color='red')
    

    # Create second line of best fit
    year_extended_2000 = year_extended[year_extended >= 2000]
    lin_regress_result_2000 = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    lin_regress_line_2000_y = lin_regress_result_2000.slope*year_extended_2000+lin_regress_result_2000.intercept
    plt.plot(year_extended_2000, lin_regress_line_2000_y, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
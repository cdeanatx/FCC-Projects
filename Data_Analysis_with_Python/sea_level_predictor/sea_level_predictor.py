import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(10, 6))
    plt.scatter(x1, y1)

    # Create first line of best fit
    (slope1, y_int1, r, p, stderr, ) = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_regress1 = range(1880, 2051, 1)
    y_regress1 = slope1 * x_regress1 + y_int1
    plt.plot(x_regress1, y_regress1, color='r')

    # Create second line of best fit
    (slope2, y_int2, r2, p2, stderr2, ) = linregress(df[df['Year'] >= 2000][['Year', 'CSIRO Adjusted Sea Level']])
    x_regress2 = range(2000, 2051, 1)
    y_regress2 = slope2 * x_regress2 + y_int2
    plt.plot(x_regress2, y_regress2, color='g')

    # Add labels and title
    plt.xlim(right=2050)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xticks(range(1850, 2076, 25))
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
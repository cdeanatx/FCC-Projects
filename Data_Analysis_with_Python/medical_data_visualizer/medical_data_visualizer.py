import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
file_to_load = 'medical_examination.csv'
df = pd.read_csv(file_to_load)

# Add 'overweight' column
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2
df.loc[df['overweight'] <= 25, 'overweight'] = 0
df.loc[df['overweight'] > 25, 'overweight'] = 1
df['overweight'] = df['overweight'].astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df_norm = df.copy()
df_norm.loc[df_norm['cholesterol'] == 1, 'cholesterol'] = 0
df_norm.loc[df_norm['cholesterol'] > 1, 'cholesterol'] = 1
df_norm.loc[df_norm['gluc'] == 1, 'gluc'] = 0
df_norm.loc[df_norm['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df_norm, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat['total'] = 1


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(kind='bar', data=df_cat, x='variable', y='total', hue='value', col='cardio', height=6, aspect=1)

    fig = g.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df_norm.loc[
        (df_norm['ap_lo'] <= df_norm['ap_hi']) & 
        (df['height'] >= df_norm['height'].quantile(.025)) & 
        (df['height'] <= df_norm['height'].quantile(.975)) &
        (df['weight'] >= df_norm['weight'].quantile(.025)) & 
        (df['weight'] <= df_norm['weight'].quantile(.975))]


    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))
    ax = sns.heatmap(df_heat.corr(), mask=mask, vmax=1, square=True, annot=True, fmt=".1f")
    

    # Draw the heatmap with 'sns.heatmap()'
    


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
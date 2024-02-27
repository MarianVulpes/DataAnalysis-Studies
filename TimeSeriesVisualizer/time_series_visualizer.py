import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("fcc-forum-pageviews.csv", header=0, index_col='date', parse_dates=True)

top_2_5_percentile = df['value'].quantile(0.975)
bottom_2_5_percentile = df['value'].quantile(0.025)
df = df[(df['value'] <= top_2_5_percentile) & (df['value'] >=  bottom_2_5_percentile)]

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def draw_line_plot():
    filtered_df_plot = df.loc[(df.index >= '2016-05-01') & (df.index < '2019-12-31')]
    plt.plot(filtered_df_plot.index, filtered_df_plot['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()

draw_line_plot()


def draw_bar_plot():
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()
    df_grouped = df_grouped.reindex(columns=months_order)
    df_grouped.plot(kind='bar', figsize=(10, 6))
    plt.title('Average Daily Page Views By Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left')
    plt.show()

draw_bar_plot()



def draw_box_plot():
    df['year'] = df.index.year
    df['month'] = df.index.month_name()

    print(df.groupby(['year', 'month'])['value'].mean().unstack())

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(data=df, x='year', y='value', ax=axes[0], color="skyblue", width=0.8, linewidth=2)
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(data=df, x='month', y='value', ax=axes[1], order=months_order, color="skyblue", width=0.8, linewidth=2)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

draw_box_plot()



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv');
df = df.sort_values(by=['value']);

# Clean data
# m = df['value'].rank(method='first').sub(1).between(0.025*len(df), 0.975*len(df),inclusive='left');
# df = df[m];
df = df[~((df['value'] < df['value'].quantile(0.025)) | (df['value'] > df['value'].quantile(0.975)))];
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d');
df.set_index('date');

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14, 7));
    sns.lineplot(x=df['date'],y=df['value']);
    ax.set(xlabel='Date', ylabel='Page Views',title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019');
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    dfc = df.copy()
    time_c= pd.to_datetime(dfc['date'], format='%Y-%m-%d');
    dfc['Months'] = time_c.dt.month_name();
    dfc['Years'] = time_c.dt.year;
    hue_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(14, 7));
    sns.barplot(x = "Years", y = "value",data = dfc, hue = "Months",errorbar=None,hue_order=hue_order,palette=sns.color_palette(n_colors=12),width=0.2);
    # fig=sns.catplot(data=dfc, x="Years", y="value", hue="Months",kind="bar",palette=sns.color_palette(n_colors=12),errorbar=None,hue_order=hue_order);
    ax.set(xlabel='Years', ylabel='Average Page Views');
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    dfc2 = df.copy()

    # Draw box plots (using Seaborn)
    time_c2= pd.to_datetime(dfc2['date'], format='%Y-%m-%d');
    dfc2['Month'] = pd.to_datetime(df['date'], format='%m').dt.strftime('%b')
    dfc2['Year'] = time_c2.dt.year;
    hue_order2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    # Yearly boxplot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6));
    sns.boxplot(data=dfc2, x="Year", y="value", hue="Year",ax=ax1,legend=None,flierprops={"marker": "d"},gap=0.2,palette=sns.color_palette(n_colors=4));
    ax1.set(xlabel='Year', ylabel='Page Views',title='Year-wise Box Plot (Trend)');
    # Monthly boxplot
    sns.boxplot(data=dfc2, x="Month", y="value", hue="Month",ax=ax2,flierprops={"marker": "d"},order=hue_order2,gap=0.5);
    ax2.set(xlabel='Month', ylabel='Page Views',title='Month-wise Box Plot (Seasonality)');
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

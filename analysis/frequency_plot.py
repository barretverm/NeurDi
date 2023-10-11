import pandas as pd

from plotnine import *

freqs = pd.read_csv('data/custom_term_freq.csv')
subcat_freqs = pd.read_csv('data/subcategory_freq.csv', )
bigcat_freqs = pd.read_csv('data/category_freq.csv')

def plot_given_freqs(df):
    
    # Convert to tidy
    df = df.rename(columns={df.columns[0]: 'Date'})
    data = df.melt(id_vars=['Date'],
                   value_vars=df.columns,
                   var_name='Categories',
                   value_name='Frequency')
    
    freq_plot = (ggplot(data, aes('Date',
                                 'Frequency',
                                 color='Categories',
                                 group='Categories')) 
                 + geom_point()
                 + geom_line())
    
    freq_plot.save(
        filename='visualizations/output/frequency_graphs/category_freq.png',
        width = 11,
        height = 8,
        units = "in")
    
plot_given_freqs(bigcat_freqs)
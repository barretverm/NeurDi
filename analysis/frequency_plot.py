import pandas as pd
from plotnine import *

def plot_given_freqs(df, filepath):
    
    # Convert to tidy
    df = df.rename(columns={df.columns[0]: 'Date'})
    df['Date'] = pd.to_datetime(df['Date'])
    data = df.melt(id_vars=['Date'],
                   value_vars=df.columns,
                   var_name='Categories',
                   value_name='Frequency')
    
    freq_plot = ggplot(data, aes('Date',
                                 'Frequency',
                                 color='Categories',
                                 group='Categories')) 
    freq_plot += geom_line()
    freq_plot += geom_point(size=1)
    freq_plot += geom_smooth()
    # freq_plot += scale_color_manual(values=['blue','red'])
    
    freq_plot.save(
        filename=filepath,
        width=20,
        height=10,
        dpi=400
        )

freqs = pd.read_csv('data/custom_term_freq.csv')
subcat_freqs = pd.read_csv('data/subcategory_freq.csv', )
bigcat_freqs = pd.read_csv('data/category_freq.csv')

work_freqs = subcat_freqs[['Unnamed: 0',
                           'General Work-related Terms',
                           'Work Environment',
                           'Work Dynamics',
                           'Work Performance',
                           'Work Schedule',
                           'Work Challenges',
                           'Work-Life Balance',
                           'Work Ethics and Values',
                           'Work Rights and Policies',
                           'Neurodiversity and Inclusion at Work',
                           'Career Development']]
lockdown_freqs = subcat_freqs[['Unnamed: 0',
                               'General Lockdown Terms',
                               'Lockdown Measures',
                               'Lockdown Impact',
                               'Lockdown Experience',
                               'Lockdown Phases and Transitions',
                               'Lockdown and Work',
                               'Lockdown and Neurodiversity']]
supervisor_freqs = subcat_freqs[['Unnamed: 0',
                                 'Supervisor Synonyms and Terms',
                                 'Additional Contextual Terms',
                                 'In the Context of Neurodiversity',
                                 'Legal and Ethical']]

# Save results to image_path
image_path = 'visualizations/output/frequency_graphs/work_freq.png'
plot_given_freqs(work_freqs, image_path)

# NOTE: lockdown_freqs is giving some errors here but the others work
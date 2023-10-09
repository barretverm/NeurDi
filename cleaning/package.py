from pathlib import Path
import pandas as pd
import pickle


years = ['2020', '2021', '2022', '2023']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

dataframes = []

for year in years:
    for month in months:
        csv_path = 'raw_data/' + year + '/' + year + '-' + month + '.csv'
        file = Path(csv_path)
        print(file)
        
        if not file.exists():
            print("Couldn't find files.")
        else:
            # Read into df
            df = pd.read_csv(csv_path)
            dataframes.append(df)

mega_df = pd.concat(dataframes)

with open('rawdata.pkl', 'wb') as file:
    pickle.dump(mega_df, file)
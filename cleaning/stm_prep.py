import pandas as pd
from pathlib import Path

def stm_prep(year, month):
    # Get cleaned data
    csv_path = 'clean/' + year + '/' + year + '-' + month + '.csv'
    file = Path(csv_path)
    if not file.exists():
        return
    
    # Read into df
    tweets_df = pd.read_csv(csv_path)
    
    tweets_df = tweets_df[['tweet_id', 'tokenized_text', 'created_at']]
    
    # Split tweets into before(0) and after(1) a particular date of the form YYYY-MM-DDTHH:MM:SS.000Z
    split_date = "2023-03-15T00:00:00.000Z"
    tweets_df["is_after_split_date"] = tweets_df['created_at'] > split_date
    
    # Simple data for R stm analysis
    tweets_df = tweets_df[['tokenized_text', 'is_after_split_date']]
    
    # Export cleaned df to csv
    filepath = Path('prepped/'+ year + '/' + year + '-' + month + '.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    tweets_df.to_csv(filepath)
    
def prep_all():        
    for year in ['2020', '2021', '2022', '2023']:
        for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            stm_prep(year, month)

stm_prep('2023','Mar')
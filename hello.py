import pandas as pd 

df = pd.read_csv('emails.csv')

df['label'] = df['spam'].apply(lambda x: 'spam' if x == 1 else 'ham')
df = df[['label', 'text']] 
df.to_csv('processed_emails.csv', index=False, header=False)
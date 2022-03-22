import pandas as pd
from datetime import date
from datetime import datetime


df = pd.read_csv('data.csv')

#################################################################################
df = df[df['date'] >= '2022-03-21']
df = df[df['event'] != 'connect']

df['rank'] = df.groupby(['date', 'chat_id', 'event']).cumcount()+1; df
df.to_csv("data_for_modufication_original.csv")

df2 = df.drop_duplicates(subset=['date', 'chat_id', 'event'], keep="last")

print("\n\ndf shape (before): ", df.shape[0])
print("df shape (after): ", df2.shape[0])

df2.to_csv("data_for_modufication.csv")

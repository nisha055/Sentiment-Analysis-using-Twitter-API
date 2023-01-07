import csv, json, sys
import pandas as pd
from pandas.io.json import json_normalize    
'''
#-----------------Positive tweets-------------------------------
df= pd.read_json('result_positive.json')
df['text'].to_csv('positive_tweet.csv', index=False)

#-----------------Negative tweets-------------------------------

df= pd.read_json('result_negative.json')
df['text'].to_csv('negative_tweet.csv', index=False)
'''

'''
#-----------------Test One month prev-----------------------------


df= pd.read_json('OneMOnthPrev.json')
df['text'].to_csv('OneMOnthPrev_tweet.csv', index=False)


#--------------------User Prev tweet-------------------------

df= pd.read_json('UserPrev.json')
df['text'].to_csv('UserPrev_tweet.csv', index=False)

'''

'''
#---------------Adding extra column with positive-1 or negative-0 ----------------------
df = pd.read_csv("positive_tweet.csv")
df['ID'] = '1'
df.to_csv('positive_tweet.csv')

df = pd.read_csv("negative_tweet.csv")
df['Label'] = '0'
df.to_csv('negative_tweet.csv')
'''


#--------------------COnvert Csv to Tsv file---------------------


import csv

with open('Data_result.csv','r') as csvin, open('Data_result_tsv.tsv', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)

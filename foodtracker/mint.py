import mintapi
import numpy
import csv
import pandas as pd

def getTransactionsMint(email, password):
    mint = mintapi.Mint(email, password)
    df_transactions = mint.get_transactions()[['date', 'description','amount','category']]
    
    return df_transactions

def getTransactionsCSV(csv_name, categories_list):
    transactions = pd.read_csv(csv_name)
    filtered_transactions = transactions[transactions['category'].isin(categories_list)]
    return filtered_transactions

#getTransactionsCSV("transactions.csv", ["restaurants", "coffee shops", "fast food"])

#print(set(mint.get_transactions()['description'].tolist()))
#cw = csv.writer(open("setofdescrip.csv",'w'))
#cw.writerow(list(set(mint.get_transactions()['description'].tolist())))

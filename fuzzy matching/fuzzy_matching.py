# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:14:41 2019

@author: shansaxena
"""

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pyodbc


cnxn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', 
                      host='XXXXXXXXX', database='XXXXXXXXX', trusted_connection='yes')                      


df = pd.read_sql_query(''' SELECT * FROM table''',cnxn )


df['FUZZY_MATCH'] = df.apply(lambda row: fuzz.token_sort_ratio(row['column1'], row['column2']), axis=1)


df.to_csv('output_fuzzy.csv')

 df.to_sql('test', con = cnxn)

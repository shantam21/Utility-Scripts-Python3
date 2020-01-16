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
                      host='USSLTCHER1012SQ.dan.sltc.com', database='PBB_V01_DAP_IA_GOOGLE_P2P_2', trusted_connection='yes')                      


df = pd.read_sql_query(''' SELECT   * FROM dbo.set_for_fuzzy_match''',cnxn )


df['FUZZY_MATCH'] = df.apply(lambda row: fuzz.token_sort_ratio(row['INV_ITEM_DESCRIPTION_1'], row['INV_ITEM_DESCRIPTION_2']), axis=1)


df.to_csv('output_fuzzy.csv')

 df.to_sql('test', con = cnxn)
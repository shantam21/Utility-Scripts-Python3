# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:02:19 2019

@author: shansaxena
"""

from pycricbuzz import Cricbuzz
c= Cricbuzz()
f = c.matches()



def getSixer(match_id):
    import time
    time.sleep(10)
    from pycricbuzz import Cricbuzz
    import re
    from interruptingcow import timeout
    c= Cricbuzz()
    data = c.commentary(match_id)
    commentary_live = data['commentary'][0]['comm']
    four = 'SIX'
    x = bool(re.findall(four,commentary_live))
    if x is True:
        print('Sixer!!')
        sendEmail()






while True:
    getSixer('22467')
    

def sendEmail():
    import win32com.client as win32
    import datetime
    import os
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'shantam.saxena@gmail.com'
    mail.Subject = 'SWiggy Sixer! Please order ASAP!! ' + datetime.date.today().strftime("%B %d, %Y")
    mail.HTMLBody = 'The batsman smashed it out of the park!! now order your food'
    mail.send
    

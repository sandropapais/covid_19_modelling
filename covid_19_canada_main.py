# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:31:46 2020

@author: Sandro
"""



import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\Sandro\Documents\GitHub\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_19-covid-Confirmed.csv")

df2 = df[df['Country/Region'].str.contains("Canada")]

#df3 = df2.drop(['Country/Region','Lat','Long'], axis=1)
df3 = df2.filter(regex='20$', axis=1)

print(df3['3/12/20'].sum())

df4 = df3.transpose()

dfSum = df4[5]+df4[92]+df4[93]+df4[94]+df4[201]+df4[406]+df4[407]+df4[411]+df4[433]+df4[434]+df4[441]


df5 = df4.rename(columns={5:"BC", 92:"ON", 93:"AB", 94:"QC", 201:"NB", 406:"MB", 407:"SK", 412:"Other", 436:"NL", 437:"PEI", 444:"NS"})

df6 = df5.drop(['1/22/20','1/23/20','1/24/20','1/25/20','1/26/20','1/27/20','1/28/20','1/29/20','1/30/20','1/31/20',
                '2/1/20','2/2/20','2/3/20','2/4/20','2/5/20','2/6/20','2/7/20','2/8/20','2/9/20','2/10/20',
                '2/11/20','2/12/20','2/13/20','2/14/20','2/15/20','2/16/20','2/17/20','2/18/20','2/19/20','2/20/20',
                '2/21/20','2/22/20','2/23/20','2/24/20','2/25/20'], axis=0)

df6.plot() 
plt.show()

dfSum.plot()
plt.show()


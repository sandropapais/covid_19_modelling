# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:31:46 2020

@author: Sandro
"""



import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\Sandro\Documents\GitHub\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv")

df2 = df[df['Country/Region'].str.contains("Canada")]

for index, row in df2.iterrows():
    if (row['Province/State'] == 'Alberta'):
        df2.rename(index={index:"AB"}, inplace=True)
    if (row['Province/State'] == 'British Columbia'):
        df2.rename(index={index:"BC"}, inplace=True)
    if (row['Province/State'] == 'Grand Princess'):
        df2.rename(index={index:"Other"}, inplace=True)
    if (row['Province/State'] == 'Manitoba'):
        df2.rename(index={index:"MB"}, inplace=True)
    if (row['Province/State'] == 'New Brunswick'):
        df2.rename(index={index:"NB"}, inplace=True)
    if (row['Province/State'] == 'Newfoundland and Labrador'):
        df2.rename(index={index:"NL"}, inplace=True)
    if (row['Province/State'] == 'Nova Scotia'):
        df2.rename(index={index:"NS"}, inplace=True)
    if (row['Province/State'] == 'Ontario'):
        df2.rename(index={index:"ON"}, inplace=True)
    if (row['Province/State'] == 'Prince Edward Island'):
        df2.rename(index={index:"PEI"}, inplace=True)
    if (row['Province/State'] == 'Quebec'):
        df2.rename(index={index:"QC"}, inplace=True)
    if (row['Province/State'] == 'Northwest Territories'):
        df2.rename(index={index:"NT"}, inplace=True)
    if (row['Province/State'] == 'Yukon'):
        df2.rename(index={index:"YT"}, inplace=True)
    if (row['Province/State'] == 'Saskatchewan'):
        df2.rename(index={index:"SK"}, inplace=True)
    if (row['Province/State'] == 'Diamond Princess'):
        df2.drop(index, axis=0, inplace=True)    
    if (row['Province/State'] == 'Recovered'):
        df2.drop(index, axis=0, inplace=True)    

df2 = df2.replace({'British Columbia':'BC', 'Alberta':'AB', 'Grand Princess':'Other',
                   'Manitoba':'MB', 'New Brunswick':'NB', 'Newfoundland and Labrador':'NL',
                   'Nova Scotia':'NS', 'Ontario':'ON','Prince Edward Island':'PEI',
                   'Quebec':'QC','Northwest Territories':'NT','Yukon':'YK',
                   'Saskatchewan':'SK'})

df2 = df2.sort_values(by=[df2[df2.columns[-1]].name],ascending=False)

for index, row in df2.iterrows():
    print(index, row['Province/State'])

#df3 = df2.drop(['Country/Region','Lat','Long'], axis=1)
df3 = df2.filter(regex='20$', axis=1)

#print(df3['3/12/20'].sum())

df3 = df3.transpose()

#dfSum = df4[5]+df4[92]+df4[93]+df4[94]+df4[201]+df4[406]+df4[407]+df4[411]+df4[433]+df4[434]+df4[441]


#df5 = df2.rename(columns={5:"BC", 92:"ON", 93:"AB", 94:"QC", 201:"NB", 406:"MB", 407:"SK", 412:"Other", 436:"NL", 437:"PEI", 444:"NS"})

df3 = df3.drop(['1/22/20','1/23/20','1/24/20','1/25/20','1/26/20','1/27/20','1/28/20','1/29/20','1/30/20','1/31/20',
                '2/1/20','2/2/20','2/3/20','2/4/20','2/5/20','2/6/20','2/7/20','2/8/20','2/9/20','2/10/20',
                '2/11/20','2/12/20','2/13/20','2/14/20','2/15/20','2/16/20','2/17/20','2/18/20','2/19/20','2/20/20',
                '2/21/20','2/22/20','2/23/20','2/24/20','2/25/20','2/26/20','2/27/20','2/28/20','2/29/20',
                '3/1/20','3/2/20','3/3/20','3/4/20','3/5/20','3/6/20','3/7/20','3/8/20','3/9/20','3/10/20'], axis=0)

ax = df3.plot() 
ax.set_title('Confirmed Cases')
ax.set_xlabel('Date')
plt.savefig('confirmed_cases.png')
plt.show()


# Yields a tuple of column name and series for each column in the dataframe
#df99 = df2.transpose()
#for (columnName, columnData) in df99.iteritems():
   #print('Colunm Name : ', columnName)
   #print('Column Contents : ', columnData.values)
   

#dfSum.plot()
#plt.show()

#ax = plt.gca()
#df.plot(kind='line',x='name',y='num_children',ax=ax)
#df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)
#plt.show()

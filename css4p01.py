# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:34:38 2024

@author: hp
"""
#import pandas library
import pandas as pd
#correct spaces in cocumn names
column_names = ['Rank','Title','Genre','Description','Director','Actors','Year','Runtime_Minutes','Rating','Votes','Revenue_Millions','Metascore']
df = pd.read_csv('movie_dataset .csv',skiprows=1, header=None, names=column_names)

# Fill nans in Revenue_Millions Column
x = df['Revenue_Millions'].mean()
df['Revenue_Millions'].fillna(x, inplace = True)

# Fill nans in Metascore Column
y = df['Metascore'].mean()
df['Metascore'].fillna(y, inplace = True)

print(df)
print(df.info())
print(df.describe(include='all'))

# highest rated movie in the dataset
highest_rated=df['Rating']==9
highest_rated_mov= df[highest_rated]
print('The highest rated movie is:',highest_rated_mov[['Rating','Title']])

# The average revenue of all movies in the dataset
print('The average revenue of all movies is:',df['Revenue_Millions'].mean())

# The average revenue of movies from 2015 to 2017 in the dataset
average_rev = (df['Year'] >= 2015) & (df['Year']<2017)
average_rev_2015_2017=df[average_rev]
print('Average revenue from 2015 to 2017 is:',average_rev_2015_2017['Revenue_Millions'].mean())

# Movies released in the year 2016
df1=df['Year'].value_counts()
print('Movies released in 2016 are:',df1[2016])

# Movies in the dataset that have a rating of at least 8.0
rated=df['Rating']>=8
rated_atleast8=df[rated]
print('Movies that are rated at least 8 are:',rated_atleast8[['Rating']].value_counts().sum())

# Movies directed by Christopher Nolan
df2=df['Director'].value_counts()
print('Movies directed by Christopher Nolan are:',df2['Christopher Nolan'])
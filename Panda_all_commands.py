#####################################################################################
###### (Part 1)_ Getting Started with Data Analysis - Installation and Loading Data #
#####################################################################################
import pandas as pd

df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv',index_col='Column')

# hany sor, hany oszlop
df.shape

# oszlop / hany db / type
df.info()

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

schema_df
schema_df.head()
schema_df.tail()

# listaban az oszlop nevek
df.columns

schema_df.loc['MgrIdiot','QuestionText']
# QuestionText    What social media site do you use the most?
# Name: SocialMedia, dtype: object

#####################################################################################
###### (Part 2)_ DataFrame and Series Basics - Selecting Rows and columns 			#
#####################################################################################


# 1....88863 - yes/no
df['Hobbyist']

df['Hobbyist'].value_counts()
# yes - 4k
# no 4k

df.iloc[0]
# elso ember [sor] valaszai [oszlopok]

df.iloc[ 0:4, 1:7]
# sorok , oszlopok

df.iloc[ 0:4, 'Hobbyist']


df[['Hobbyist','Employment']]

#####################################################################################
###### (Part 3)_ Indexes - How to Set, Reset, and Use Indexes						#
#####################################################################################

schema_df.sort_index(ascending=False)

high_salary = ( df['ConvertedComp'] > 70000 )
high_salary
# true/false oszlop

df.loc[high_salary,['Country','LanguageWorkedWith','ConvertedComp']]


countries = ['Hungary','Slovakia','Russia']
filtCounties = df['Country'].isin(countries)

df.loc[filtCounties,'Country']

filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
df.loc[filt,'LanguageWorkedWith']



#####################################################################################
###### (Part 8) Grouping and Aggregating - Analyzing and Exploring Your Data		#
#####################################################################################


# median-ja az oszlopnak : 

df['ConvertedComp'].median()

# mindenhol ahol ertelmezve lehet, mediant nez, oszlop
df.median()


df.describe()

# count	5.594500e+04	5.582300e+04	64503.000000	49790.000000	79210.000000
# mean	5.519014e+11	1.271107e+05	42.127197	5.084308	30.336699
# std	7.331926e+13	2.841523e+05	37.287610	5.513931	9.178390
# min	0.000000e+00	0.000000e+00	1.000000	0.000000	1.000000
# 25%	2.000000e+04	2.577750e+04	40.000000	2.000000	24.000000
# 50%	6.200000e+04	5.728700e+04	40.000000	4.000000	29.000000
# 75%	1.200000e+05	1.000000e+05	44.750000	6.000000	35.000000
# max	1.000000e+16	2.000000e+06	4850.000000	99.000000	99.000000

# az osszes megadott ertek 80k = 50k kitoltotte + 30k NaN
df['ConvertedComp'].count()
# 55823

df['SocialMedia'].value_counts()
# Reddit                      14374
# YouTube                     13830
# WhatsApp                    13347
# Facebook                    13178
# Twitter                     11398
# Instagram                    6261
# I don't use social media     5554
# LinkedIn                     4501
# WeChat 微信                     667
# Snapchat                      628
# VK ВКонта́кте                 603
# Weibo 新浪微博                     56
# Youku Tudou 优酷                 21
# Hello                          19

# in percantage
df['SocialMedia'].value_counts(normalize=True)


# orszagok group by-olva
country_grp = df.groupby(['Country'])

# osszes oszlop magyarorszagra
country_grp.get_group('Hungary')

# the filter is the give thesame result
filt = df['Country'] == 'Hungary'
df.loc[filt]['SocialMedia'].value_counts()

# country_grp['SocialMedia'].value_counts().head(50)
# country_grp['SocialMedia'].value_counts().loc['Romania']
country_grp['SocialMedia'].value_counts(normalize=True).loc['Hungary']


country_grp['ConvertedComp'].median().loc['Hungary']

country_grp['ConvertedComp'].agg(['median','mean']).loc['Hungary']
# median    26412.000000
# mean      33823.553191


filt = df['Country'] == 'Hungary'
df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()

country_grp['LanguageWorkedWith'].apply( lambda x: x.str.contains('Python').sum() )
# Country
# Afghanistan                              8
# Albania                                 23
# Algeria                                 40
# Andorra                                  0
# Angola                                   2

# Szazalek szamitas, az orszagban az osszes progger kozul hany % pythonos
country_respondent = df['Country'].value_counts()
country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())    

merged_df = pd.concat([country_respondent,country_uses_python], axis = 'columns', sort = False)
merged_df
# 	Country	LanguageWorkedWith
# United States	20949	10083
# India	9061	3105
# Germany	5866	2451
# United Kingdom	5737	2384
# Canada	3395	1558
# ...	...	...
# North Korea	1	0
# Saint Kitts and Nevis	1	0
# Saint Vincent and the Grenadines	1	0
# Timor-Leste	1	1
# Papua New Guinea	1	0
merged_df.rename(columns={'Country':'NumCorespondents','LanguageWorkedWith':'WorkedWithPy'},inplace=True)

# (part / whole ) * 100
merged_df['pctNumKnowPy'] = (merged_df['WorkedWithPy'] / merged_df['NumCorespondents'] ) * 100
merged_df

merged_df.sort_values(by='pctNumKnowPy',ascending=False,inplace=True)
merged_df
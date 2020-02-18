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
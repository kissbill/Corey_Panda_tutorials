people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


import pandas as pd
# #########################################################################################################

df = pd.DataFrame(people)

type(df['email'])

# ##################### Coulmns location ###############################################################
df.columns

# integer location
# 0. row
df.iloc[0]
# sorok
df.iloc[ [0,2] ]
# sorok , oszlopok
df.iloc[ [0,2], 2]
# szovegesen email oszlop megadhato
df.loc[[1,2],['email','last']]
#  uj index megadasa
df.set_index('email',inplace=True)
df.index
# index sor , es oszlop lekerdezese
df.loc['CoreyMSchafer@gmail.com','last']
# index reset 
df.reset_index(inplace=True)

# ##################### Filtering ###############################################################

df['last'] == 'Doe'

filt = (df['last'] == 'Doe')

df[filt]

# ahol filter ervenyes annak a sornak az oszlopat kiadja 
df.loc[filt,'email']

# multiple filer
filt = (df['last'] == 'Doe') & (df['first'] == 'John')
df.loc[filt,'email']
# negaltja : 
df.loc[filt,'email']

# ##################### Coulmns renaming ###############################################################

df.columns
df.columns = ['first_name','last_name','email']

df.columns = [x.upper() for x in df.columns] 

df.columns = df.columns.str.replace('_',' ')

df.rename(columns = {'FIRST NAME': 'first','LAST NAME':'last'},inplace = True)

# ertek bevitel 
df.loc[2] = ['John','Smith','JohnSmith@email.com']
df.loc[2,['last','EMAIL']] = ['Doe','johndoe@email.com']

 filt = (df['EMAIL'] == 'johndoe@email.com')
 df.loc[filt,'last'] = 'Smith'

# csak kiijra kis betuvel
 df['email'].str.lower()
# fel is veszi az kis betus ertekeket
df['email'] = df['email'].str.lower()

# hossza az email-eknek
df['email'].apply(len)


def update_email(email):
    return email.upper()
# igy nem hajtodik vegre egybol
df['email'].apply(update_email)

# ezzel viszont igen()
# df['email'].apply( update_email() )

# ertek atadassal replace lesz
df['email'] = df['email'].apply(update_email)

# lambdaval megoldva inline fgv
df['email'] = df['email'].apply(lambda x: x.lower())

df.apply(len)
# mibol hany db elem van adott oszlopban
# Out[34]:
# first_name    3
# last_name     3
# email         3

# oszlop hany elemes
len(df['email'])

df.apply(len,axis='columns')

# minden oszlopbol a legkisebb erteket veszi
df.apply(pd.Series.min)
df.apply(lambda x: x.min())

# map, mindenbol mi mennyi van
# adott sorban kirja Corey -> 5 , Doe -> 3 , email -> 5
df.applymap(len)


df.applymap(str.lower)


df['first_name'].map({'Corey':'jani','jane':'Johanna'})
# igy ahol nem adtunk erteket, not a number lesz

df['first'].replace({'Corey':'jani','Jane':'Johanna'})
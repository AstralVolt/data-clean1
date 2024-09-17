import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

#df.dropna(inplace=True)
print(df)
df.info()

#Step 1:
#Fill the empty Cells


#df['Calories'].fillna(df['Calories'].mean(), inplace=True)
df['Calories'] = df['Calories'].fillna(df['Calories'].mean())
# print(df)
# df.info()
df['Calories_mean'] = df['Calories'].fillna(df['Calories'].mean())
df['Calories_median'] = df['Calories'].fillna(df['Calories'].median())
df['Calories_mode'] = df['Calories'].fillna(df['Calories'].mode()[0])
df['Golden_no'] = df['Calories'].fillna(230)
print(df)

# Best possible value is normal skewed curve/bell curve

plt.boxplot([df.Calories_mean, df.Calories_median, df.Calories_mode, df.Golden_no], vert= False)
plt.show()

#Step 2
# Data of Wrong Format
# to_datetime()

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df)

df.dropna(inplace = True)
df.info()

#Step 3
#Correcting abnormal data

for var in df.index:
    if df.loc[var, 'Duration'] > 150:
        if df.loc[var, 'Duration'] == 450:
            df.loc[var, 'Duration'] = 45
        elif df.loc[var, 'Duration'] == 300:
            df.loc[var, 'Duration'] = 30
        elif df.loc[var, 'Duration'] == 600:
            df.loc[var, 'Duration'] = 60
        else:
            df.loc[var, 'Duration'] = 150


#Step 4
#Duplicate Data

print(df.duplicated())
df.drop_duplicates(inplace = True)
df.info()
print(df)


df.to_csv('Data_cleaned.csv', index= False)
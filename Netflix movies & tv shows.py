import pandas as pd

df = pd.read_csv('C:/Users/Pallak Sinha/Desktop/Files for data analysis/netflix_titles.csv')  # full file path
print(df.head())
print(df.shape) 
print(df.info())       
print(df.describe())   

print(df['type'].value_counts())

if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'])
    print(df['date_added'].dt.year.value_counts().sort_index())
    
print(df.isnull().sum())

missing_percent = df.isnull().mean() * 100
print(missing_percent.sort_values(ascending=False))

df['director'] = df['director'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')

print(df.isnull().sum())

df = df.drop_duplicates()
print(df.shape) 
print(df.info())  

df['country'] = df['country'].str.strip().str.lower()
df['type'] = df['type'].str.strip().str.title()
df['director'] = df['director'].str.replace(r'\s+', ' ', regex=True)

df['country'].value_counts()
df[df['type'] == 'Movie']

print(df[['type', 'title', 'country']].head())
print(df[['type', 'date_added', 'release_year']].head())

if 'date_added' in df.columns:
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')  # dd-mm-yyyy format

        df['year_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year
        df['month_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.month_name()
print(df[['type', 'date_added', 'release_year']].head())

df['year_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year
df['month_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.month_name()
print(df[['type', 'month_added', 'year_added','country']].head())








    

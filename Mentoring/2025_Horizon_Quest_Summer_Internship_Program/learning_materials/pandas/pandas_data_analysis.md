# Data Analysis with Pandas

This document introduces basic data analysis using `pandas` and `numpy`. It covers reading various CSV formats and performing common operations like filtering, grouping, reshaping, and numerical computation.

## 📥 Reading CSV Files

```python
import pandas as pd

# Basic read
df = pd.read_csv('data.csv')

# With custom delimiter (\t means tab)
df = pd.read_csv('data.tsv', delimiter='\t')

# Reading with specific encoding, utf-8 is very popular encoding.
df = pd.read_csv('data.csv', encoding='utf-8')

# Reading a URL-hosted CSV
url = 'https://raw.githubusercontent.com/path/to/file.csv'
df = pd.read_csv(url)
```

## 🔧 Basic Data Manipulation

```python
# Inspecting data
df.head()
df.info()
df.describe()

# Selecting columns and rows
df['column_name']
df.loc[5]
df.iloc[0:10]

# Filtering
df[df['column'] > 50]

# Adding a new column
df['new_col'] = df['col1'] + df['col2']

# Dropping columns
df.drop('unnecessary_col', axis=1, inplace=True)

# Handling missing values
df.fillna(0)
df.dropna()

# Grouping
df.groupby('category_col')['value_col'].mean()

# Merging
pd.merge(df1, df2, on='id')

# Sorting
df.sort_values(by='score', ascending=False)
```

## 🔢 Using NumPy with Pandas

```python
import numpy as np

# Apply NumPy function
df['log_value'] = np.log(df['value'])

# Conditional creation
df['flag'] = np.where(df['score'] > 80, 'High', 'Low')
```

---

## ❓ Questions & Answers

1. **Q:** How do you read a tab-separated CSV file?  
   **A:** Use `pd.read_csv('file.tsv', delimiter='\t')`.

2. **Q:** How can you read only the first 100 rows of a large CSV file?  
   **A:** Use `pd.read_csv('file.csv', nrows=100)`.

3. **Q:** What's the difference between `.loc[]` and `.iloc[]`?  
   **A:** `.loc[]` is label-based; `.iloc[]` is integer-position-based.

4. **Q:** How do you rename columns in a dataframe?  
   **A:** `df.rename(columns={'old_name': 'new_name'}, inplace=True)`.

5. **Q:** How do you find all missing values in a column?  
   **A:** `df['column'].isna().sum()`.

6. **Q:** How do you select rows where column "A" is greater than 100?  
   **A:** `df[df['A'] > 100]`.

7. **Q:** How do you change the datatype of a column to integer?  
   **A:** `df['column'] = df['column'].astype(int)`.

8. **Q:** What does `df.describe()` do?  
   **A:** It shows summary statistics for numeric columns.

9. **Q:** How do you apply a function to every row?  
   **A:** Use `df.apply(my_function, axis=1)`.

10. **Q:** How can you concatenate two dataframes vertically?  
    **A:** `pd.concat([df1, df2], axis=0)`.

11. **Q:** How do you fill missing values with the median?  
    **A:** `df['col'].fillna(df['col'].median(), inplace=True)`.

12. **Q:** How do you group by multiple columns?  
    **A:** `df.groupby(['col1', 'col2']).mean()`.

13. **Q:** How do you filter a dataframe using multiple conditions?  
    **A:** `df[(df['A'] > 50) & (df['B'] == 'Yes')]`.

14. **Q:** How do you find the unique values of a column?  
    **A:** `df['col'].unique()`.

15. **Q:** How do you compute a cumulative sum?  
    **A:** `df['col'].cumsum()`.

16. **Q:** How do you drop duplicate rows?  
    **A:** `df.drop_duplicates(inplace=True)`.

17. **Q:** How do you create a pivot table?  
    **A:** `df.pivot_table(index='A', columns='B', values='C')`.

18. **Q:** How do you apply a NumPy `log` transformation?  
    **A:** `np.log(df['column'])`.

19. **Q:** How do you find correlation between columns?  
    **A:** `df.corr()`.

20. **Q:** How can you save a modified dataframe to CSV?  
    **A:** `df.to_csv('output.csv', index=False)`.


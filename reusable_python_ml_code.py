#standard imports
import pandas as pd
from pandas import DataFrame, Series


#-----------------------------------------------------            Basic data manipulations

#print unique counts in a categorical variable
df[['<list of columns>']].nunique()


# find if a list is in another ilst
is_in_df =  df[df["column"].isin(second_df['column'])]

#Sorting 
df.sort_values(by="column_name", ascending=False)


#identifying pairs 
from itertools import premutations

def find_pairs(x)
  pairs = pd.DataFrame(list(permutations(x.values, 2)), 
                       columns = ['col_1','col_b'])
  return pairs

df.groupby('group_col')['subset_col'].apply(find_pairs)

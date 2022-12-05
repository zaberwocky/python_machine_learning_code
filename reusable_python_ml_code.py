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

#find occurences
df.groupby(['col_1','col_2']).size()


#crosstabulation or transposing
pd.corsstab(df['col1'], df['col2']) # first column becomes rows and second becomes columns with 1 and 0

#------------------------------------------------------               Statistics

#jaccard similarity 
from sklearn.metrics import jaccard_score
jaccard_score(row1, row1)

#finding distance between all items using Jaccard
from scipy.distance import pdist, squareform
jaccard_distances = pdist(df.values, metric = 'jaccard')
square_jaccard_distances = squareform(jaccard_distances) 


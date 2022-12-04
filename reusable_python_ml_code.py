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


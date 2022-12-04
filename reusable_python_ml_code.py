#standard imports
import pandas as pd
from pandas import DataFrame, Series


#-----------------------------------------------------            Summary Satistics

#print unique counts in a categorical variable
df[['<list of columns>']].nunique()


# find if a list is in another ilst
is_in_df =  df[df["column"].isin(second_df['column'])]

import pandatex as pdtex
import pandas as pd

df = pd.DataFrame({
    'Discipline':['Math','Portuguese','Math','Portuguese','Math','Portuguese'],
    'Class':['A','A','B','B','C','C'],
    'Average Grade':[9.0,6.0,7.3,6.0,9.3,7.5]})
    
table = pdtex.TexTable(name="DogsAndCats",dataframe=df)

table.writetextable()
# PandaTex

## What is PandaTex?

PandaTex is a package to transform Pandas data tables into .tex files

## Getting started

### Install the package
To install the package you can use the Pypi using the command 

```
pip install PandaTex
```

### Example

Input
```
import pandatex as pdtex
import pandas as pd

df = pd.DataFrame({
    'Discipline':['Math','Portuguese','Math','Portuguese','Math','Portuguese'],
    'Class':['A','A','B','B','C','C'],
    'Average Grade':[9.0,6.0,7.3,6.0,9.3,7.5]})
    
table = pdtex.TexTable(name="AvGrades",caption="Table with the data",label="Table",dataframe=df)

table.printtextable()
```

Output
```
\begin{table}[htb!]
\centering
\begin{small}
\caption{Table with the data}\label{Table}
\begin{tabular}{*{4}{|c}|}
\hline
  & Discipline & Class & Average Grade \\ \hline
0 & Math & A & 9.0 \\ \hline
1 & Portuguese & A & 6.0 \\ \hline
2 & Math & B & 7.3 \\ \hline
3 & Portuguese & B & 6.0 \\ \hline
4 & Math & C & 9.3 \\ \hline
5 & Portuguese & C & 7.5 \\ \hline
\end{tabular}
\end{small}\end{table}
```
If you want to generate a .tex file with the dataframe from the example above you can use the method "writetextable"

```
table.filename = 'myDocs'
table.writetextable()
```
---
## TexTable
### Constructor

**TexTable**(name= "", filename="Default",label = " ", caption = " ", dataframe = None)

## Functions
**TexTable.printtextable(\*\*kwargs):**
This function can be used to print the result of the pandas table in latex format

**TexTable.writetextable(\*\*kwargs):**
This function can be used to write a .tex file with the result of the pandas table in latex format

When printing or writing tables you can use some included arguments to format the table

## **kwargs

* **coltype** (default:"grid" or ["indexed","nogrid"])
This argument controls.

<!--* **overfill** (default:"scale" or ["newtable","encode"]) This argument controls how should the table deal with extra wide tables
    * scale - scale the table down to fit the content
    * newtable - create a new table to fit the remaining content
    * encode - create a list that encodes each column -->
* **align** (default:"c" or ["l", "r"]) This argument controls the alignment of the data.
    * c - align center
    * l - align left
    * r - align right
* **indexed** (dtype: boolean, default:True) This argument can be deactivated if the table does not contain indexes.
* **hlines** (dtype: boolean, default:True) This argument can be deactivated if you want to remove the horizontal lines from the table.

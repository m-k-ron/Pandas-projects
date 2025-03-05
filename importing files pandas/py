# importing file from downloads 
from os import sep
import pandas as pd
pd.read_csv('/Users/hubertkrajewski/Downloads/countries of the world.csv')

# changing headers
import pandas as pd
pd.read_csv('/Users/hubertkrajewski/Downloads/countries of the world.csv', header = None)

# assigning to a variable
import pandas as pd
df = pd.read_csv('/Users/hubertkrajewski/Downloads/countries of the world.csv')
df 

# importing text file
import pandas as pd
df = pd.read_csv('/Users/hubertkrajewski/Downloads/countries of the world.txt')
df 

# separating columns
import pandas as pd
df = pd.read_csv('/Users/hubertkrajewski/Downloads/countries of the world.txt', sep = '\t' )
df 

# reading txt file as table
import pandas as pd
df = pd.read_table('/Users/hubertkrajewski/Downloads/countries of the world.txt')
df 

# reading cvs file as table
import pandas as pd
df = pd.read_table('/Users/hubertkrajewski/Downloads/countries of the world.csv', sep = ',')
df 

# reading json file as table
import pandas as pd
df = pd.read_json('/Users/hubertkrajewski/Downloads/json_sample.json')
df 

# reading excel file
df2 = pd.read_excel('/Users/hubertkrajewski/Downloads/world_population_excel_workbook.xlsx', sheet_name = 'Sheet1')
df2 

# showcasing all rows 
pd.set_option('display.max_rows', 234)

# showcasing all columns 
pd.set_option('display.max_columns', 40)

# database info
df2.info() 

# database table shape (number of columns and rows)
df2.shape

# looking at top 10 rows 
df2.head(10)

# looking at bottom 10 rows
df2.tail(10) 

# looking at rank column
df2['Rank']

# looking at 224th row
df2.loc[224]

df2.iloc[224]

import pandas as pd
from datetime import datetime
df = pd.read_csv(r"C:/Users/Harish/Downloads/data.csv")

def convert_date(col):
    col = datetime.strptime(col,'%m/%d/%y %H:%M')
    return col

def convertDate_toString(col):
    col = col.strftime('%Y-%m-%d %H:%M')
    return col

# convert Person Id from Int to Str as per Json schema
df['Person Id'] = df['Person Id'].apply(str)
# convert floor access datetime to python datetime object
df['Floor Access DateTime'] = df['Floor Access DateTime'].apply(convert_date)
# convert datetime object to str type as per json schema
df['Floor Access DateTime'] = df['Floor Access DateTime'].apply(convertDate_toString)
# write pandas dataframe to output json file
df.to_json(r'C:/Users/Harish/Downloads/data.json')

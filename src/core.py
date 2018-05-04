from pandas import read_csv
from pandas import Series
from pandas import DataFrame
import datetime

series = read_csv('usage/usage-2018-05-10.csv',
            names=['date','folder','size'],
            header=0,
            index_col=0,
            parse_dates=[0])
#print series.tail(10)
#print(series['2018-05-10 23-45'])
df = DataFrame(series)
#print df.loc['2018-05-10 23:40:00':'2018-05-10 23:50:00']
df_recent = df.loc[datetime.datetime(2018, 5, 10,23,40,0):datetime.datetime(2018, 5, 10,23,50,0)]
print df_recent
total=int(df_recent.loc[df_recent['folder'] == '/log','size'].item())
df_recent['percentage'] = (df_recent['size']/total)*100
print df_recent

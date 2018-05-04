from pandas import read_csv
from pandas import Series
from pandas import DataFrame
import pandas
import datetime
import os
import glob
import re

# series = read_csv('usage/usage-2018-05-10.csv',
#             names=['date','folder','size'],
#             header=0,
#             index_col=0,
#             parse_dates=[0])
# #print series.tail(10)
# #print(series['2018-05-10 23-45'])
# df = DataFrame(series)
# #print df.loc['2018-05-10 23:40:00':'2018-05-10 23:50:00']
# df_recent = df.loc[datetime.datetime(2018, 5, 10,23,40,0):datetime.datetime(2018, 5, 10,23,50,0)]
# print df_recent
# total=int(df_recent.loc[df_recent['folder'] == '/log','size'].item())
# df_recent['percentage'] = (df_recent['size']/total)*100
# print df_recent

class CSVReader:
    def __init__(self, usage_location):
        self.path = usage_location
        self.df = DataFrame()

    def getBetweenDates(self, start_date, end_date):
        all_files = glob.glob(os.path.join(self.path,"*"))
        list_ = []
        series = None
        for f in all_files:
            file_date_match = re.search(r'\d{4}-\d{2}-\d{2}', f)
            file_date = datetime.datetime.strptime(file_date_match.group(), '%Y-%m-%d').date()
            if (file_date >= start_date and file_date <= end_date):
                if 'gz' in f:
                    series = read_csv(f,
                                      names=['date','folder', 'size'],
                                      header=0,
                                      index_col=0,
                                      parse_dates=[0],
                                      compression='gzip'
                                      )
                else:
                    series = read_csv(f,
                                      names=['date','folder', 'size'],
                                      header=0,
                                      index_col=0,
                                      parse_dates=[0],
                                      )
                list_.append(series)
        df = pandas.concat(list_)
        return df.sort_index()

    def getLatest():
        pass



if __name__ == "__main__":
    start_date=datetime.datetime.strptime('2018-05-06', '%Y-%m-%d').date()
    end_date=datetime.datetime.strptime('2018-05-07', '%Y-%m-%d').date()
    reader = CSVReader('/home/arun/Projects/bingoarun/sizemonitor/usage')
    print reader.getBetweenDates(start_date,end_date)
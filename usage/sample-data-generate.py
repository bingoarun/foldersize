import datetime
import random
import numpy as np

Today=datetime.datetime(2018, 5, 1)
start_size=2000000000000

dir_example=['/log',
             '/log/veg',
             '/log/fruit',
             '/log/veg/tomato',
             '/log/veg/brinjal',
             '/log/fruit/orange',
             '/log/fruit/apple',
             '/log/fruit/grapes'
            ]
size = {key:0 for key in dir_example}

date_list = [Today + datetime.timedelta(minutes=15*x) for x in range(0, 960)]
for i in date_list:
    size['/log/fruit/grapes'] = size['/log/fruit/grapes'] + random.randint(10000,20000)
    size['/log/fruit/orange'] = size['/log/fruit/orange'] + random.randint(10000,20000)
    size['/log/fruit/apple'] = size['/log/fruit/apple'] + random.randint(10000,20000)
    size['/log/fruit'] = size['/log/fruit/apple'] + size['/log/fruit/orange'] + size['/log/fruit/grapes']
    size['/log/veg/tomato'] = size['/log/veg/tomato'] + random.randint(5000,20000)
    size['/log/veg/brinjal'] = size['/log/veg/brinjal'] + random.randint(5000,20000)
    size['/log/veg'] = size['/log/veg/brinjal'] + size['/log/veg/tomato']
    size['/log'] = size['/log/veg'] + size['/log/fruit']
    for d in dir_example:
        print("%s,%s,%d" % (i,d,size[d]))
        name='usage-'+i.strftime("%Y-%m-%d")+'.csv'
        with open(name,"a") as myfile:
            print name
            myfile.write("%s,%s,%d\n" % (i,d,size[d]))

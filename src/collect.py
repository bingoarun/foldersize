#!/bin/python
''' 
This is a standalone Python script to collect usage details 
for foldermon application. 
Schedule this script in cron for every 15 mins.
Eg:
*/15 * * * * python /etc/sizemonitor/collect.py /myfolder >> /var/usage/usage-`date +"\%Y-\%m-\%d"`.csv | /usr/bin/logger -t sizemonitor
Here /myfolder the folder to be monitored and /var/usage/ is the folder where usage data will be saved. 
'''

import os
import datetime
import sys
from os.path import join, getsize

dirs_dict = {}

if len (sys.argv) != 2 :
    print "Usage: python collect.py <directory> \n Eg: python collect.py /logs"
    sys.exit (1)

for root, dirs, files in os.walk(sys.argv[1],topdown = False):
    size = sum(getsize(join(root, name)) for name in files)
    subdir_size = sum(dirs_dict[join(root,d)] for d in dirs)
    my_size = dirs_dict[root] = size + subdir_size
    print '%s,%s,%d'%(datetime.datetime.now(),root,my_size)
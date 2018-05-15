# folmon
WIP : A simple tool to monitor folder and sub-folder sizes over time. It is ideal for setting up in a remote server environment where you can't have any time-series DB or can't install any agents (or daemons) to monitor a particular folder, as the collection script in this tool uses cron and doesn't run anything in the background.

## Usage

#### Get overall size status of a particular folder
```
$ folmon status
+---------------------+-------------------+----------+------------+
|         date        |       folder      | size(MB) | percentage |
+---------------------+-------------------+----------+------------+
| 2018-05-10 23:45:00 |        /log       |  64.518  |   100.0    |
| 2018-05-10 23:45:00 |      /log/veg     |  23.101  |   35.806   |
| 2018-05-10 23:45:00 |     /log/fruit    |  41.417  |   64.194   |
| 2018-05-10 23:45:00 |  /log/veg/tomato  |  11.654  |   18.063   |
| 2018-05-10 23:45:00 |  /log/veg/brinjal |  11.447  |   17.743   |
| 2018-05-10 23:45:00 | /log/fruit/orange |  13.773  |   21.348   |
| 2018-05-10 23:45:00 |  /log/fruit/apple |  13.94   |   21.607   |
| 2018-05-10 23:45:00 | /log/fruit/grapes |  13.703  |   21.24    |
+---------------------+-------------------+----------+------------+
```

#### Get difference in size of folder between specific dates

```
$ folmon diff -s 2018-05-05 -e 2018-05-07 -f /log/fruit
+---+-------------------+------------+------------+---------------------+
|   |       folder      | 2018-05-05 | 2018-05-07 | percentage_increase |
+---+-------------------+------------+------------+---------------------+
| 0 |     /log/fruit    |   16.621   |   28.968   |        74.292       |
| 1 |  /log/fruit/apple |   5.573    |   9.773    |        75.371       |
| 2 | /log/fruit/grapes |   5.513    |   9.572    |        73.639       |
| 3 | /log/fruit/orange |   5.535    |   9.624    |        73.856       |
+---+-------------------+------------+------------+---------------------+

$ folmon diff -s 2018-05-05 -e 2018-05-10 -f /log/
+---+-------------------+------------+------------+---------------------+
|   |       folder      | 2018-05-05 | 2018-05-10 | percentage_increase |
+---+-------------------+------------+------------+---------------------+
| 0 |     /log/fruit    |   16.621   |   41.417   |       149.191       |
| 1 |  /log/fruit/apple |   5.573    |   13.94    |       150.157       |
| 2 | /log/fruit/grapes |   5.513    |   13.703   |       148.585       |
| 3 | /log/fruit/orange |   5.535    |   13.773   |       148.823       |
| 4 |      /log/veg     |   9.248    |   23.101   |       149.801       |
| 5 |  /log/veg/brinjal |    4.59    |   11.447   |       149.404       |
| 6 |  /log/veg/tomato  |   4.658    |   11.654   |       150.193       |
+---+-------------------+------------+------------+---------------------+
```

## Installation instructions

#### Setup collection script

Download the collection script (https://github.com/bingoarun/folmon/blob/master/collect/collect.py) and place it under specific folder (i.e /etc/sizemonitor/collect.py ) 

Add the following entry in cron where '/myfolder' is the folder you want to start monitoring and '/etc/sizemonitor/collect.py' is the location of the downloaded collection script.
```
*/15 * * * * python /etc/sizemonitor/collect.py /myfolder >> /var/usage/usage-`date +"\%Y-\%m-\%d"`.csv | /usr/bin/logger -t sizemonitor
```

#### Install the cli agent
(If you don't want to install the CLI agent, you can skip this and follow the next step)
```
$ pip install folmon
```

#### Running script directly without installing the CLI command
(Skip this, if you have installed the agent via pip in the previous step)

```
$ git clone https://github.com/bingoarun/folmon.git
$ cd folmon
$ python command/__init__.py  diff -s 2018-05-05 -e 2018-05-07 -f /log/
+---+-------------------+------------+------------+---------------------+
|   |       folder      | 2018-05-05 | 2018-05-07 | percentage_increase |
+---+-------------------+------------+------------+---------------------+
| 0 |     /log/fruit    |   16.621   |   28.968   |        74.292       |
| 1 |  /log/fruit/apple |   5.573    |   9.773    |        75.371       |
| 2 | /log/fruit/grapes |   5.513    |   9.572    |        73.639       |
| 3 | /log/fruit/orange |   5.535    |   9.624    |        73.856       |
| 4 |      /log/veg     |   9.248    |   16.175   |        74.908       |
| 5 |  /log/veg/brinjal |    4.59    |   8.041    |        75.183       |
| 6 |  /log/veg/tomato  |   4.658    |   8.134    |        74.636       |
+---+-------------------+------------+------------+---------------------+
```
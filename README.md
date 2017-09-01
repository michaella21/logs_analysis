# logs_analysis
This repository contains files to create a plain text report file based on the data (newsdata.sql) in the database. logs_analysis.py file connects the PostgreSQL server using the `psycopg2` module. This file finds answers for the followin 3 questions:

  1. _What are the most popular three articles of all time?_
  2. _Who are the most popular article authors of all time?_
  3. _On which days did more than 1% of requests lead to errors?_

To run this file, bring the virtual machine back online (with `vagrant up`) and log into it with `vagrant ssh`. Keep the logs_analysis.py file with newsdata.sql into `vagrant` directroy. By typint `psql -d news -f newsdata.sql`, load the data. logs_anaysis.py file is written in Python3 and to run it by `Python3 logs_anasis.py`. Since this file runs 3 quite heavy loaded queries, it may take some time to finish it. However,  you should be able to find a file name `log_anaysis.txt` file in the same directory. The sample output is also contained in this repository. 
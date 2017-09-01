# LOGS_ANALYSIS
This repository contains files to create a plain text report file based on the data (newsdata.sql) in the database. This data is assumed to be collected from a fictional news website, which includes the access requests made for 31 days for the articles in this fictional news website. You can find the following three tables in newsdata.sql.

* _articles_: information about each article including title, author(id only,  foreign key, refering authors.id), slug for the url path and other details. 
* _authors_: information about each authors name, bio and id.
* _log_: information about the access requests including path, status code (200 or 404) , the time when each request was made, etc.

Both logs_analysis.py and logs_analysis_ver2.py files connects the PostgreSQL server using the `psycopg2` module. (You are free to choose any file to use) It finds answers for the followin 3 questions:

  1. _What are the most popular three articles of all time?_
  2. _Who are the most popular article authors of all time?_
  3. _On which days did more than 1% of requests lead to errors?_

## Requirements
To use newsdata.sql as well as the file included in this repository, Linux based virtual machine is required. You can download [VBox](https://www.virtualbox.org/wiki/Downloads) and [vagrant](https://www.vagrantup.com/downloads.html) from each link and install them as directed. Once virtual machine is installed, you can download [the configuration file](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile). You can bring the virtual machine back online (with `vagrant up`) and log into it with `vagrant ssh`.

## Data
You can download the [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). After downloading and unzipping it, put the newsdata.sql file in the same `vagrant` directory. To load the data, type in `psql -d news -f newsdata.sql`. Once data is loaded, you can connect to the data and explore it by `psql news`. 

## Running the script
To run this file, load the data as directed above, bring the virtual machine back online (with `vagrant up`) and log into it with `vagrant ssh`. Keep the **logs_analysis.py** or **logs_analysis_ver2.py** file with newsdata.sql into `vagrant` directroy. 

Both logs_anaysis.py and logs_analysis_ver2.py files are written in Python3 and to run it by `python3 logs_anasis.py`. Since this file runs 3 quite heavy loaded queries, it may take some time to finish it. However, you should be able to find a file name `anaysis.txt` file in the same directory. The sample output is also contained in this repository. 




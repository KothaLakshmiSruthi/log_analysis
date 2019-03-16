# Project 3: Logs Analysis Project
# by KOTHA LAKSHMI SRUTHI


## About the logAnalysis project

A Reporting page that prints out reports in a plain text format based on the data in the database.This reporting tool is a python program using the `psycopg2` module to connect to the database.

# Questions used to be solved while working on logAnalysis project

* query for Most popular three articles of all time are?
* query for Most popular article authors of all time are?
* query for Day on which more than 1% of requests lead to errors?

## items which are included in my folder logAnalysis

This project consists for the following files are:

* logAnalysis.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this some tools which are required
* newsdata.sql - database file which contains some tables
		Tables:
			articles
			authors
			log
* log_output.JPG - my sample output is involved
* views1.sql - views which are created to solve the required questions

## Tools which are required to perform logAnalysis project

1. Python
2. Vagrant
3. VirtualBox
4. postgresql

## Dependencies

- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd /vagrant` as instructed in terminal

## Steps to run the logAnalysis project
	
	Windows users will need commant prompt to execute the program

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  
  
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  
  3. download newsdata.sql

  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

  5. Copy the newsdata.sql file and place inside `vagrant/logAnalysis
  
  6. Change the directory by entering
  
  ```
	$ cd vagrant
  ```
  
   7. connect to postgres in vagrant:
   
   ```
	 $ sudo su - postgres
   ```
   
   8. change/connect to postgres:
   
   ```
	 $ psql
   ```
   
   9. come out from postgres
   
   ```
	 $ \q 
	 $ logout
   ```

   10. Load the data in local database using the command:

   ```
     $ psql -d news -f newsdata.sql
   ```
  
   11. creating views to perform queries
   
    ```
	 $ psql -d news -f views1.sql
	```

   12. Run logAnalysis.py using:
   
   ```
     $ python logAnalysis.py
   ```
  
  Note: generating queries will take several seconds to execute 

# My sample Output:
![log_output.jpg](https://github.com/KothaLakshmiSruthi/log_analysis/blob/master/log_output.jpg)

# Project 3: Logs Analysis Project
### by KOTHA LAKSHMI SRUTHI

Logs Analysis Project, part of the Udacity [Full Stack Web Developer
Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## What it is and does

A Reporting page that prints out reports in a plain text format based on the data in the database.This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Project content

This project consists for the following files are:

* logAnalysis.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* newsdata.sql - database file
* log_output.JPG

## Required Tools

1. Python
2. Vagrant
3. VirtualBox
4. postgresql

## Installation

There are some dependancies and a few instructions on how to run the application.

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

## How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/logs-analysis`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

  5. Copy the newsdata.sql file and place inside `vagrant/logAnalysisProject
  
  6. connect to vagrant:
  ```
	$ cd vagrant
  ```
  
   7. connect to postgresql in vagrant:
   ```
	 $ sudo su - postgresql
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
  
   views required:
		
		view1:(``` view for most popular articles ```)
			CREATE VIEW articleswhoarepopular as SELECT replace(path,'/article/','') as slug, count(*) as views
			FROM log
			WHERE path<>'/' AND status ='200 OK' GROUP BY path;
			
		view2:(``` view to print the error ```)
			create view fail as select date(time),round(100.0*sum(case log.status
			when '200 OK'  then 0 else 1 end)/count(log.status),3) as error
			from log group
			by date(time) order by error desc;
	
  
   12. Load the data in local database using the command:
   ```
     $ psql -d news -f views1.sql
   ```
   
   13. Run logAnalysis.py using:
   ```
     $ python logAnalysis.py
   ```
  
  Note: queries will take sometime to execute 

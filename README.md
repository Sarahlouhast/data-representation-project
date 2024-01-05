### Programming for Data Representation Project
### Course: Higher Diploma in Data Analytics
### Module: Data Representation
### Year & Semester: 2023 - 02
### Student: Sarah Hastings
### ID: G00235562

***

### Getting started
This repository contains the project for the Data Representation Module Winter 2023:24 https://github.com/Sarahlouhast/data-representation-project.

The project objective - Build a basic Flask server that has a REST API to perform CRUD operations include one database table and a web interface, using AJAX calls, to perform these CRUD operations.

The project details can viewed here https://github.com/andrewbeattycourseware/datarepresentation/blob/main/project/Project%20Description.pdf.

The repository contains the following files:
* README.md file
* .gitignore - GitHub gitignore file
* initdb.sql - file contains SQL statements to create database
* dbconfig.py (dbconfig_template.py) - configuration file contains MySQL database details
* ProductDAO.py - Data Access Object python file to interact with database
* ProductDAOTest.py - test the ProductDAO file
* requirements.txt - text file with python packages required to run the app
* server.py - Flask server application
* static_pages - folder contains html page and images


#### Database Description
A database 'prod_data' is used to store product information, the user is able to create, update, delete and make any changes to any of the products. It contains a table called 'productdata' which has the following data fields:

ID (PRIMARY KEY, AUTO-INCREMENT)
Product
Manufacturer        
Model            
Price

Clone repository: https://github.com/Sarahlouhast/data-representation-project

Create and activate blank virtual environment with a directory named venv. Anaconda was used to create a localhost virtual environment (venv) for running the server. It can be installed using the Anaconda python distribution, https://www.anaconda.com/. The following Windows command line python commands can used be to create the venv, install and save the necessary packages for the venv, set the flask_app server and server mode, run the server, stop the server and finally deactivate the venv.

Make a virtual environment  	python -m venv venv
Make a virtual environment with system packages 	python -m venv venv --system-site-packages
Run a virtual environment	 .\venv\Scripts\activate.bat
See the packages	pip freeze
Save them to a file 	pip freeze > requirements.txt
Load a file of packages 	pip install -r requirements.txt
exit	deactivate

For this projoect I use the below to install the necessary packages and added to my requirements.txt.

(venv)λ pip install Flask
(venv)λ pip install mysql-connector-python
(venv)λ pip freeze > requirements.txt

The package requirements can also be installed from the list in the file 'requirement.txt' using the venv command

(venv)λ pip install -r requirements.txt

The dbconfig.py file contains specific details for each machine and user. A template version of this file 'dbconfigtemplate.py' is included in this repository. This template has to edited to match the specific requirements for each machine the database is running on. My file is saved locally as 'dbconfig.py' for the DAO to read it, the gitignore file ignores this file to ensure it is not uploaded for security purposes. A connection pool is used to make database connections.

MySQL is used to implemented the database. The user can create the database, its associated table and populate the initial database content by using the 'initdb.sql', all this data is stored in this initialisation file.

ProductDAO.py is a Database Access Object (DAO) for the products, an instance of this can be called with an associated python server to undertake CRUD operations on the database. 

Flask Server 
A server app called 'server.py', uses Python flask for dealing with requests and responses for database CRUD operations. The server file can be run locally from the command line by typing the command 'python server.py' or via a local or remote virtual environment.

Run Flask server (On Windows):
SET FLASK_APP=server
SET FLASK_ENV=development
flask run
Open http://127.0.0.1:5000/ 

A database graphical user interface page 'index.html' is included the 'staticpages' folder of this repository. This was designed in HTML for use on the Google Chrome browser. The interface page uses the latest Bootstrap CSS sheet styles from https://getbootstrap.com/ and AJAX/jQuery library from https://developers.google.com/speed/libraries. This interface can be used to view and undertake CRUD operations on the database content. Once the app server is running, the interface page can be accessed from a web browser via the root url address using a localhost 'http://127.0.0.1:5000/index.html'.




_________________

The repository contains:

This README.md file
Files that form the Web application project option.
.gitignore - includes reference to dbconfig.py and venv, so that when it is downloaded, the repository won't damage that person's own configuration.
dbconfig.py - the purpose of the configuration file is to create the initial settings for the project. A newuser will need to amend the template file, dbconfig_template, to include their own local settings (e.g., user name and password) before proceeding.
requirements.txt - This file is a list of the specific python packages and versions detail required to run this project. The user can install the required packages using requirements.txt:
Open a terminal or command prompt
Navigate to the folder with requirements.txt
run: pip install -r requirements.txt
Installation of dependencies is complete.
server.py - The server program is simple, with the “heavy lifting” carried out in the DAO.
ProductDAO.py - This program that consumes an API, it defines the standard CRUD operations to be performed.
ProductDAOTest.py- I have included to show the process and to test the functionality of the ProductDAO file to ensure functions are working as expected.
index.html - This is the accompanying web interface, AJAX calls perform the CRUD operations and this file is saved in the staticpages folder.
foodie.ico - a favicon that provides a small food themed image displayed in the browser address bar of index.html 
initdb.sql- This is the initialisation file. Using mysql this file will create the database, its associated table and populate the initial database content. In mysql you can use SOURCE along with the local of the file path for this file to action it.


### Instructions for downloading this repository
Log on to GitHub and search for user Sarahlouhast, the repository is entitled data-representation-project, https://github.com/Sarahlouhast/data-representation-project. You can chose click on the code button and chose to clone the repository or download as a zip file onto your machine. For further information on how github works video guides are available here https://www.youtube.com/githubguides.

#### How to run the files and view the functionality of this project

Open a terminal or command prompt
Navigate to the folder with requirements.txt
run: pip install -r requirements.txt
Installation of dependencies is complete.

After download and installation of requirments.txt, open server.py on the command line
Confirmation that this file has linked to the Data Access Object (DAO) is printed to the screen
Connection @ init made with ProductDAO.py
The Flask app is being served!
Cut and paste local host URL that appears on the screen into a browser.
http://127.0.0.1:5000/index.html will bring you to a Welcome page displaying "Welcome to the Product API Page"
Database contents can be view in json format at http://127.0.0.1:5000/products
Navigate to http://127.0.0.1:5000/index.html which is the landing page index.html to displayall available products. 
Options are Add New products, Update or Delete current products.
The buttons are colour coded, a bootstrap convention to convey meaning.
When creating a new product, the program will only accept numerical values in the price field.
Select "Go Back" if there is no requirement to create a new item.

### References
All references used in this project are listed below.

* https://docs.python-guide.org/dev/virtualenvs/
* https://github.com/andrewbeattycourseware/datarepresentation/tree/main/code
* https://martin-thoma.com/configuration-files-in-python/
* https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
* https://github.com/Slawak1/Data-Representation-Project
* https://github.com/ClodaghMurphy/dataRepresentationProject
* https://github.com/markcot/ProjDataRep/blob/main/README.md
* https://favicon.io/emoji-favicons/laptop/
* https://www.tutorialspoint.com/flask/flask_sessions.htm
* https://pynative.com/python-database-connection-pooling-with-mysql/
* https://www.geeksforgeeks.org/flask-tutorial/
* https://docs.github.com/en/rest
* https://flask.palletsprojects.com/en/latest/
* https://icons8.com/icons

***

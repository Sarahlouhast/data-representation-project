### Course: Higher Diploma in Data Analytics
### Module: Data Representation
### Year & Semester: 2023 - 02
### Student: Sarah Hastings
### ID: G00235562

***

### Getting started
This repository contains the project for the Data Representation Module Winter 2023:24 https://github.com/Sarahlouhast/data-representation-project.

The project objective: Build a basic Flask server that has a REST API to perform CRUD operations include one database table and a web interface, using AJAX calls, to perform these CRUD operations.

The project details can viewed here,  https://github.com/andrewbeattycourseware/datarepresentation/blob/main/project/Project%20Description.pdf.

### Contents of the repository
This repository contains the following files:

1. README.md file - Detailing the project and the files that form the project.

2. .gitignore - GitHub gitignore file - includes reference to dbconfig.py and venv to ignore these files, both are stored locally for security purposes.

3. dbconfig_template.py - Template configuration file contains MySQL database details, the purpose of the configuration file is to create the initial settings for the project. A newuser will need to amend the template file to include their own local settings (e.g., user name and password) before proceeding. dbconfig.py is stored locally for security purposes.

4. requirements.txt - This file is a list of the specific python packages and versions detail required to run the app. The user can install the required packages using the requirements.txt:

* Open a terminal or command prompt
* Navigate to the folder with requirements.txt
* run: pip install -r requirements.txt
* Installation of dependencies is complete.

5. initdb.sql - This is the initialisation file. Using MySQL this file will create the database, its associated table and populate the initial database content. In MySQL you can use SOURCE along with the location of the file path for this file to action it.

6. ProductDAO.py - This program consumes an API, it defines the standard CRUD operations to be performed. It acts as a Database Access Object (DAO) for the products, an instance of this can be called with an associated python server to undertake CRUD operations on the database. 

7. ProductDAOTest.py- I have included this file to show the process and to test the functionality of the ProductDAO file to ensure functions are working as expected.

8. server.py - Flask server application, this file uses Python flask for dealing with requests and responses for database CRUD operations. 

9. static_pages - This folder contains html page and favicon image

10. it.ico - a favicon that provides an IT themed image displayed in the browser address bar of index.html and this file is saved in the staticpages folder.

11. img - folder containing png files showing content from index.html page, products page, findById page, also png files showing database content and structure 

12. index.html - This is the accompanying web interface html page, AJAX calls perform the CRUD operations and this file is saved in the staticpages folder. This was designed in HTML for use on the Google Chrome browser. The interface page uses the latest Bootstrap CSS sheet styles from https://getbootstrap.com/ and AJAX/jQuery library from https://developers.google.com/speed/libraries. This interface can be used to view and undertake CRUD operations on the database content. Once the app server is running, the interface page can be accessed from a web browser via the root url address using a localhost 'http://127.0.0.1:5000/index.html'.

### Database Description
The database used for this project is called 'prod_data'. It is used to store product information, the user is able to create, update, delete and make any changes to any of the products. It contains a table called 'productdata' which has the following data fields:

* ID (PRIMARY KEY, AUTO-INCREMENT)
* Product
* Manufacturer        
* Model            
* Price

### Download the repository
Log on to GitHub and search for user Sarahlouhast, the repository is entitled data-representation-project, https://github.com/Sarahlouhast/data-representation-project. You can chose click on the code button and chose to clone the repository or download as a zip file onto your machine. For further information on how github works video guides are available here https://www.youtube.com/githubguides.

### Run & view the functionality of this project
Create and activate blank virtual environment with a directory named venv. Anaconda was used to create a localhost virtual environment (venv) for running the server. It can be installed using the Anaconda python distribution, https://www.anaconda.com/. The following Windows command line python commands can used be to create the venv, install and save the necessary packages for the venv, set the flask_app server and server mode, run the server, stop the server and finally deactivate the venv.

* Make a virtual environment  	python -m venv venv
* Make a virtual environment with system packages 	python -m venv venv --system-site-packages
* Run a virtual environment	 .\venv\Scripts\activate.bat
* See the packages	pip freeze
* Save them to a file 	pip freeze > requirements.txt
* Load a file of packages 	pip install -r requirements.txt
* exit	deactivate

For this projoect I used the below to install the necessary packages and added to my requirements.txt.

* (venv)λ pip install Flask
* (venv)λ pip install mysql-connector-python
* (venv)λ pip freeze > requirements.txt

The package requirements can also be installed from the list in the file 'requirements.txt' using the venv command

* (venv)λ pip install -r requirements.txt

After download and installation of requirments.txt, open the dbconfig_template.py and edit with your specific details for machine and user. 

Next you can run the initdb.sql on MySQL to create a copy of database.

After these steps are completed the user can open server.py on the command line. 
Confirmation that this file has linked to the Data Access Object (DAO) is printed to the screen.
Connection @ init made with ProductDAO.py.
The Flask app is being served!

Next copy and paste the local host URL that appears on the screen into a browser, http://127.0.0.1:5000 will bring you to a Welcome page displaying "Welcome to the Product API Page".
Database contents can be viewed in json format at http://127.0.0.1:5000/products.
Navigate to http://127.0.0.1:5000/index.html which is the landing page /index.html to display all available products and perform CRUD operations. Options are Add New products, Update or Delete current products. 
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

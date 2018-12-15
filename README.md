# Suave-Apps

In order for the flask app to run the database must have one column on each table as a primary key
Then, from the web folder, run app.py to view flask pages for index & app, as well as JSON APIs
 
the report link: https://docs.google.com/document/d/10aQpftZebJuCNBOhSaoe_vgQXpkKFKIj193J0dm9Lik/edit?usp=sharing

ETL Project - Team 1 (The Suaves)

Objectives:
Use Kaggle data sources for Apple and Android mobile app data and extract/transform/load data to MySQL database
Create a flask API that serves up JSON representation of the mobile app data 
Create a flask API that takes in a route variable and returns various JSON depending on at least one query param.
A bootstrap website that displays a subset of the mobile app data in a visually appealing table.
BONUS: Create a link on our homepage to another page which documents the API.
Data Sources
Kaggle.com
Content Ratings were updated according to ESRB ratings table found here.

Datasets
	Google Play Store Apps
	Mobile App Store ( 7200 apps) 

Process
	EXTRACTION
All Datasets downloaded from Kaggle as CSV files
The following columns were used for Apple:
AppleStore.csv:
id
track_name
size_bytes
price
user_rating
cont_rating
prime_genre
appleStore_description.csv:
id
track_name
app_desc
The following columns were used for Android:
 Android data file:
Application name
Category
Rating
Size
Price
Content Rating

TRANSFORMATION
Using Pandas and Python within a Jupyter Notebook, read in both datasets and the Apple App store descriptions data with ‘pd.read_csv()’
Rename column names with a letter ‘a’ or ‘g’ in front of the name to distinguish the source dataset
Remove apps that do not appear in both data sets by using ‘.drop duplicate’ 
Convert the Apple app size values into megabytes(Mb) from bytes
Round app size values to 1 decimal place
Remove non-numeric characters from app size columns
Remove rows containing “varies with device” in app size columns (goog data)
Drop any rows still containing errors
Remove “$” from price data
Create new DataFrame to identify equivalent content ratings
Rename content ratings from 1 to 4 to match with new content rating DataFrame
Reset index


 LOAD
(SQLite)
Create the connection to the SQLite DB
Create the engine with ‘create_engine('sqlite:///app_info.db')’
Create tables ['apple_descriptions', 'apps', 'apps_test']
Add main DataFrame to SQLite database
Add Apple descriptions to SQLite database
Read Apple descriptions table back into python with pandas to verify correct load
Export Apple descriptions data frame as a CSV file 

(MySQL)
Create app_db database with MySQL workbench (apps_schema.sql file)
Create tables ['apple_description', 'apps'] with id column as there primary key
On python, notebook create a connection to the database 
Convert the tables we have to SQL to be in the tables we create on app_db

Flask App / API version
Flask app is connected to MySQL database.
It has 2 routes home and info to display the elt project app, and 3 routs for the Json APIs.
To run it:
 from the web folder, run app.py to view flask pages for index & app, as well as the flask APIs
(In order for the flask app to run the database must have one column on each table as a primary key)

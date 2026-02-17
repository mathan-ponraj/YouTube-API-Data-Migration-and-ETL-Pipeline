# YouTube Trending Data ETL using Python, SQLAlchemy and SQLite

## General info  
The project includes an end-to-end ETL (Extract, Transform, Load) process using Python, SQLAlchemy, and SQLite to collect and analyze trending YouTube video data.  
This ETL workflow automatically extracts data from the YouTube Data API, transforms raw JSON data into a clean and structured format, and loads it into a SQLite database for SQL-based analysis.  

ETL stands for Extract, Transform, and Load and it is a fundamental workflow in data engineering. The purpose of ETL is to collect data from external sources, clean and transform it, and store it in a database for analysis and reporting.  

## Dataset  
The dataset is generated dynamically using the YouTube Data API and contains information about trending videos such as:  
- Video title  
- Channel name  
- Views  
- Likes  
- Comments  
- Publish date  
- Engagement metrics  

The processed data is stored in CSV format and in a SQLite database (`youtube_trending.db`).  

## Project includes  
ETL scripts for data extraction, transformation, and loading  
Main execution script to run the complete ETL workflow  
SQLite database for storing transformed data  
SQLAlchemy for database connection and loading  
Automated data collection and analytics process  

## Summary  
The project consists of classical ETL steps:

### 1. Extract:  
This stage is used to extract data from the YouTube Data API.  
I used Python to fetch trending video data and converted the API response into Pandas DataFrames for further processing.  

### 2. Transform:  
This stage is used to clean and transform the raw data.  
In this step I have:  
- Handled missing and inconsistent values  
- Removed duplicate records  
- Converted data types for analysis  
- Created new features like engagement rate (likes per views)  
- Structured the dataset into analysis-ready format  

### 3. Load:  
The final stage is used to load the transformed data into the database.  
I used SQLite database with SQLAlchemy engine to store the cleaned dataset into relational tables, making the data query-ready for SQL analysis and reporting.  

## Technologies  
Project is created with:  
- Python 3  
- SQL (SQLite)  
- SQLAlchemy  
- Pandas, NumPy  
- YouTube Data API  

## Running the project  
To run the complete ETL workflow:

```bash
python main.py
```
## About

An end-to-end YouTube Trending Data ETL project that demonstrates API data extraction, data transformation with pandas, and database loading using SQLAlchemy, along with SQL-based analytics for real-world data engineering and data analyst use cases.

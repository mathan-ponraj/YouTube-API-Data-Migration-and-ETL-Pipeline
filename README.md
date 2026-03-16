# YouTube API Data Migration & ETL Pipeline

## Project Overview
This project demonstrates an automated **ETL (Extract, Transform, Load) pipeline** that collects and processes trending video data from the YouTube Data API.

The system extracts raw data from the API, processes **nested JSON responses**, cleans and transforms the data, and stores the structured dataset in a **SQL database** for further analysis.

The main goal of this project was to build a **reliable data pipeline** that converts raw API data into structured datasets that can be easily queried and analyzed.

---

## Problem Statement
YouTube generates a large amount of video data every day. However, the data returned by the API is in **nested JSON format**, which is difficult to analyze directly.

To make the data useful, the raw API responses must be:

- Collected automatically from the API  
- Parsed from nested JSON structures  
- Cleaned and validated  
- Converted into structured tables  
- Stored in a relational database  

This project solves these challenges by building a **Python-based ETL pipeline**.

---

## System Workflow

API Extraction → JSON Processing → Data Cleaning → Data Transformation → SQL Storage

---

## Data Extraction (API Integration)

The project uses the **YouTube Data API** to collect trending video information.

An API key created through **Google Cloud Console** is used to make automated API requests.

The pipeline collects important fields such as:

- Video Title  
- Channel Name  
- View Count  
- Like Count  
- Comment Count  
- Video Category  
- Publish Date  

The API responses are returned in **JSON format**.

---

## JSON Data Processing

The API responses contain **nested JSON objects**. Python scripts were used to parse and extract the required information.

Key steps included:

- Parsing JSON API responses  
- Extracting nested attributes  
- Converting JSON data into tabular format  
- Handling missing or inconsistent values  

This step transforms raw API responses into structured datasets.

---

## Data Transformation and Cleaning

After extracting the data, several preprocessing steps were applied:

- Removing unnecessary attributes  
- Handling missing values  
- Standardizing column formats  
- Preparing the dataset for database storage  

These steps help ensure the dataset is **clean, consistent, and ready for analysis**.

---

## Automated ETL Pipeline

A Python-based **ETL pipeline** was built to automate the workflow.

### Extract
Data is collected automatically from the YouTube Data API.

### Transform
Python scripts process the JSON responses, clean the data, and convert it into structured tables.

### Load
The cleaned dataset is stored in a **SQL database** using **SQLAlchemy**, which allows efficient querying and analysis.

---

## Data Storage

The processed dataset is stored in a **relational SQL database**.  
This makes it easy to run queries, perform aggregations, and analyze trends in the data.

---

## Results

### Automated Data Pipeline
Developed an automated workflow to extract, transform, and load YouTube API data.

### Structured Dataset
Converted raw nested JSON responses into structured SQL tables.

### Trend Analysis
Created datasets that allow analysis of video engagement and trending content.

---

## Technologies Used

- Python  
- Pandas  
- SQL  
- SQLAlchemy  
- YouTube Data API  
- JSON Data Processing  

---

## Key Outcomes

- Implemented **API-based automated data extraction**
- Built a **Python ETL pipeline**
- Processed and cleaned nested JSON API responses
- Converted unstructured API data into structured SQL tables
- Generated datasets for **YouTube trend analysis**

---

## Future Improvements

- Automate scheduled API data collection  
- Build interactive dashboards for visualization  
- Apply machine learning models for trend prediction  

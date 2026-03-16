# Creator Economy Analytics: Mining Trends from YouTube API Data

## Project Overview
With the rapid growth of video content on YouTube, analyzing trending video data helps understand audience behavior and content popularity.

This project builds an **automated ETL pipeline** to collect, preprocess, and analyze trending video data using Python, SQL, and the YouTube Data API.

The system automatically extracts raw data from the API, processes JSON responses, performs data preprocessing, and loads the cleaned dataset into a structured SQL database for further analysis.

---

## The Challenge
YouTube generates massive amounts of data every day. The main challenge was collecting and analyzing trending video data in a structured and automated way.

The raw data from the YouTube Data API is delivered in **nested JSON format**, which makes it difficult to analyze directly using traditional database queries.

Key challenges included:

- Handling complex nested JSON API responses  
- Extracting only relevant attributes from large API datasets  
- Managing API request limits  
- Cleaning inconsistent or missing values  
- Converting unstructured API data into structured tables for analysis  

---

## Data Extraction using API
A developer API key was created through Google Cloud to access the YouTube Data API.

Using this key, automated API requests were made to collect trending video data such as:

- Video title  
- Channel name  
- View count  
- Like count  
- Comment count  
- Video category  
- Publish date  

The API responses were received in **JSON format**.

---

## JSON Data Handling
The API response contained nested JSON objects. Python was used to parse and extract required fields from the JSON response.

Key steps included:

- Parsing JSON API responses  
- Extracting nested attributes  
- Converting JSON data into tabular datasets  
- Handling missing or inconsistent values  

---

## Data Preprocessing
After extracting the JSON data, preprocessing steps were applied to improve data quality:

- Removing unnecessary fields  
- Handling missing values  
- Data formatting and normalization  
- Structuring the dataset for database storage  

---

## Automated ETL Pipeline
To automate the workflow, an **ETL (Extract, Transform, Load) pipeline** was developed.

**Extract**  
Data was automatically collected from the YouTube Data API.

**Transform**  
Python scripts processed the JSON responses, cleaned the data, and converted it into structured tabular format.

**Load**  
The cleaned dataset was stored in a relational SQL database using SQLAlchemy for efficient querying and analysis.

---

## Data Storage
The processed dataset was loaded into a SQL database, enabling efficient querying, aggregation, and trend analysis.

---

## Results

**Automated Data Pipeline**  
Built an automated workflow for extracting, transforming, and loading YouTube API data.

**Clean and Structured Dataset**  
Converted raw nested JSON API responses into a structured database format.

**Trend Insights**  
Identified engagement patterns and popular video categories among trending content.

---

## Technologies Used
- Python  
- SQL  
- Pandas  
- SQLAlchemy  
- YouTube Data API  
- JSON Data Handling  

---

## Key Outcomes
- Implemented **API-based automated data extraction**
- Built a **Python-based ETL pipeline**
- Processed and cleaned nested JSON API responses
- Converted unstructured API data into structured SQL tables
- Generated datasets for **YouTube trend analysis**

---

## Future Improvements
- Build interactive dashboards for visualization
- Implement machine learning models for trend prediction
- Automate scheduled API data collection

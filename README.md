# YouTube Trending Videos Analytics

## Project Overview
This project is an automated ETL (Extract, Transform, Load) system designed to migrate data from the YouTube Data API into a structured SQL environment. I built this to solve the challenge of handling large-scale, nested JSON responses and converting them into high-quality, query-ready data for business analysis.

## The Problem
Raw data from modern APIs is often deeply nested and messy. To make YouTube trending data actually useful for a business, it needs to be extracted reliably, parsed from complex JSON structures, cleaned for consistency, and stored in a relational database. Manual exports are too slow; an automated pipeline is the only scalable solution.

## My Technical Workflow

1. Automated Extraction: I integrated the YouTube Data API v3 to programmatically fetch metadata, including engagement metrics (views, likes, comments) and content categories.
2. JSON Transformation: Since API responses are nested, I developed a parsing logic in Python to flatten the JSON objects into a tabular format, ensuring no data loss during the conversion.
3. Data Cleaning: I implemented a transformation layer to handle missing values, standardize date-time formats, and remove duplicate entries.
4. Database Loading: Using SQLAlchemy, I built the "Load" portion of the pipeline to migrate the processed data into a SQL database. This allows for fast, relational queries that aren't possible with raw JSON.

## System Architecture
**API Extraction** (JSON) ➔ **Python Processing** (Pandas) ➔ **Data Transformation** ➔ **SQL Storage** (SQLAlchemy)

## Key Features
- Dynamic API Handling: Manages API requests and handles data points like Video Title, Channel, and Category.
- Structured Storage: Replaces unstructured files with a robust SQL schema.
- Scalability: The Python-based logic is designed to be easily scheduled for daily or hourly data syncs.

## Tools and Technologies
- Language: Python
- Data Libraries: Pandas, JSON, NumPy
- Database & ORM: SQL, SQLAlchemy
- External Integration: YouTube Data API v3 (Google Cloud Console)

## Future Goals
To evolve this into a production-grade data platform, I plan to:
- Containerize the pipeline using Docker for easier deployment.
- Schedule the script using Apache Airflow or GitHub Actions for fully hands-off automation.
- Build a monitoring layer to alert me if the API fails or data formats change.

---
Developed by Mathan Ponraj
CSE Graduate | Data & Systems Engineering
[LinkedIn Profile](https://www.linkedin.com)

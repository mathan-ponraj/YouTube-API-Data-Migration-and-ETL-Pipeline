# YouTube Trending Data Pipeline and Analytics

## Case Study

**Problem**  
Trending YouTube data is dynamic, unstructured, and difficult to analyze without an automated pipeline. Manual analysis does not scale and limits insights into views, likes, and engagement patterns.

**Context**  
This project simulates a real-world data engineering workflow by collecting live data from the YouTube Data API, transforming it, storing it in a relational database, and performing SQL-based analytics.

**Impact**  
The pipeline enables repeatable, query-ready analytics on trending YouTube videos, supporting insights such as top-performing content, channel dominance, and engagement efficiency.

**Why It Matters**  
Demonstrates end-to-end data engineering skills, including API ingestion, data transformation, database design, and analytical querying.

---

## What I Did

- Built an automated data ingestion pipeline using the YouTube Data API
- Cleaned and transformed raw API data into analytics-ready format
- Designed and populated a SQLite database
- Performed SQL-based exploratory and analytical queries
- Exported analytical outputs for downstream reporting

---

## How I Did It (STAR Format)

**Situation**  
Raw YouTube trending data is API-driven, inconsistent, and not analysis-ready.

**Task**  
Design a scalable pipeline to collect, clean, store, and analyze trending video data.

**Action**  
- Integrated YouTube Data API using Python
- Implemented data transformation and deduplication using Pandas
- Loaded cleaned data into SQLite for structured querying
- Wrote optimized SQL queries for engagement and performance analysis
- Modularized the pipeline into ingestion, transformation, loading, and analytics scripts

**Result**  
- Fully automated ETL pipeline
- Query-ready relational database
- Actionable insights on views, likes, and engagement ratios
- Reusable architecture adaptable to other APIs or regions

---

## Tech Stack

- Programming Language: Python  
- APIs: YouTube Data API v3  
- Data Processing: Pandas, NumPy  
- Database: SQLite  
- Querying: SQL  
- Configuration Management: Environment Variables  
- Storage: CSV, SQLite  

---

## Key Results / Business Impact

- Automated collection of trending YouTube videos by region
- Reduced manual data handling through ETL automation
- Enabled ranking of videos and channels by:
  - Total views
  - Total likes
  - Engagement rate (likes per view)
- Produced exportable analytics datasets for reporting and dashboards

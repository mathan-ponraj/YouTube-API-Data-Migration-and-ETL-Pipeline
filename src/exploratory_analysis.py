"""
exploratory_analysis.py

Purpose:
Run SQL-based exploratory data analysis (EDA)
on YouTube Trending data stored in SQLite database.
"""

import sqlite3
import pandas as pd
import os

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
DB_PATH = os.path.join("data", "youtube_trending.db")


# --------------------------------------------------
# DB HELPER
# --------------------------------------------------
def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# --------------------------------------------------
# EDA ANALYSIS
# --------------------------------------------------
def perform_eda():
    print("\n🚀 Starting Exploratory Data Analysis...\n")

    # 1. Total videos
    q1 = "SELECT COUNT(*) AS total_videos FROM youtube_trending;"
    print("📊 Total Videos:")
    print(run_query(q1), "\n")

    # 2. Unique channels
    q2 = "SELECT COUNT(DISTINCT channel) AS unique_channels FROM youtube_trending;"
    print("📊 Unique Channels:")
    print(run_query(q2), "\n")

    # 3. Top 10 most viewed videos
    q3 = """
        SELECT title, channel, views
        FROM youtube_trending
        ORDER BY views DESC
        LIMIT 10;
    """
    print("📊 Top 10 Most Viewed Videos:")
    print(run_query(q3), "\n")

    # 4. Top 10 most liked videos
    q4 = """
        SELECT title, channel, likes
        FROM youtube_trending
        ORDER BY likes DESC
        LIMIT 10;
    """
    print("📊 Top 10 Most Liked Videos:")
    print(run_query(q4), "\n")

    # 5. Channels with most videos
    q5 = """
        SELECT channel, COUNT(*) AS video_count
        FROM youtube_trending
        GROUP BY channel
        ORDER BY video_count DESC
        LIMIT 10;
    """
    print("📊 Channels with Most Videos:")
    print(run_query(q5), "\n")

    # 6. Engagement rate (likes / views)
    q6 = """
        SELECT title,
               channel,
               views,
               likes,
               ROUND((likes * 1.0 / views) * 100, 2) AS engagement_percent
        FROM youtube_trending
        WHERE views > 0
        ORDER BY engagement_percent DESC
        LIMIT 10;
    """
    print("📊 Top Engagement Videos:")
    print(run_query(q6), "\n")

    print("✅ Exploratory Data Analysis Completed!")


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":
    perform_eda()

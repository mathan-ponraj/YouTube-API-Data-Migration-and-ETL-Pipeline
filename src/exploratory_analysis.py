"""
exploratory_analysis.py

Purpose:
Perform SQL-based Exploratory Data Analysis (EDA)
on YouTube Trending data stored in a SQLite database.
This analysis helps understand video performance,
channel dominance, and engagement patterns.
"""

import sqlite3
import pandas as pd
import os

# CONFIG
DB_PATH = os.path.join("data", "youtube_trending.db")



# DATABASE HELPER FUNCTION

def run_query(query):
    """Execute SQL query and return results as DataFrame"""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# EXPLORATORY DATA ANALYSIS

def perform_eda():
    print("\nStarting Exploratory Data Analysis on YouTube Trending Dataset...\n")

    # 1. Dataset overview
    print("1. Dataset Overview")
    overview_query = "SELECT COUNT(*) AS total_videos FROM youtube_trending;"
    print(run_query(overview_query), "\n")

    # 2. Unique channels analysis
    print("2. Unique Channels Analysis")
    unique_channels_query = """
        SELECT COUNT(DISTINCT channel) AS unique_channels
        FROM youtube_trending;
    """
    print(run_query(unique_channels_query), "\n")

    # 3. Top 10 most viewed videos
    print("3. Top 10 Most Viewed Videos")
    top_viewed_query = """
        SELECT title, channel, views
        FROM youtube_trending
        ORDER BY views DESC
        LIMIT 10;
    """
    print(run_query(top_viewed_query), "\n")

    # 4. Top 10 most liked videos
    print("4. Top 10 Most Liked Videos")
    top_liked_query = """
        SELECT title, channel, likes
        FROM youtube_trending
        ORDER BY likes DESC
        LIMIT 10;
    """
    print(run_query(top_liked_query), "\n")

    # 5. Channels with highest number of trending videos
    print("5. Channels with Highest Number of Trending Videos")
    channel_dominance_query = """
        SELECT channel, COUNT(*) AS video_count
        FROM youtube_trending
        GROUP BY channel
        ORDER BY video_count DESC
        LIMIT 10;
    """
    print(run_query(channel_dominance_query), "\n")

    # 6. Average engagement metrics
    print("6. Average Engagement Metrics (Views, Likes, Comments)")
    avg_metrics_query = """
        SELECT 
            ROUND(AVG(views), 2) AS avg_views,
            ROUND(AVG(likes), 2) AS avg_likes,
            ROUND(AVG(comments), 2) AS avg_comments
        FROM youtube_trending;
    """
    print(run_query(avg_metrics_query), "\n")

    # 7. Top engagement rate videos (likes/views)
    print("7. Top 10 Videos by Engagement Rate")
    engagement_query = """
        SELECT 
            title,
            channel,
            views,
            likes,
            ROUND((likes * 1.0 / views) * 100, 2) AS engagement_percent
        FROM youtube_trending
        WHERE views > 0
        ORDER BY engagement_percent DESC
        LIMIT 10;
    """
    print(run_query(engagement_query), "\n")

    # 8. Most active publish dates (trend frequency)
    print("8. Most Active Publish Dates")
    publish_trend_query = """
        SELECT publish_date, COUNT(*) AS video_count
        FROM youtube_trending
        GROUP BY publish_date
        ORDER BY video_count DESC
        LIMIT 10;
    """
    print(run_query(publish_trend_query), "\n")

    print("Exploratory Data Analysis Completed Successfully.")



# ENTRY POINT

if __name__ == "__main__":
    perform_eda()

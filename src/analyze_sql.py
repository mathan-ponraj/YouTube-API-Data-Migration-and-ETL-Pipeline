import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join("data", "youtube_trending.db")

def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def analyze_data():
    print("\n===== SQL ANALYSIS =====\n")

    # 1. Top viewed videos
    print("Top 5 Most Viewed Videos:")
    q1 = """
        SELECT title, channel, views, likes
        FROM trending_videos
        ORDER BY views DESC
        LIMIT 5;
    """
    print(run_query(q1), "\n")

    # 2. Channels with highest total views
    print("Top Channels by Total Views:")
    q2 = """
        SELECT channel, SUM(views) AS total_views
        FROM trending_videos
        GROUP BY channel
        ORDER BY total_views DESC
        LIMIT 5;
    """
    print(run_query(q2), "\n")

    # 3. Best Like/View ratio
    print("Videos with Best Like/View Ratio:")
    q3 = """
        SELECT title, channel, likes, views,
               ROUND(CAST(likes AS FLOAT)/views, 4) AS ratio
        FROM trending_videos
        ORDER BY ratio DESC
        LIMIT 5;
    """
    print(run_query(q3), "\n")

if __name__ == "__main__":
    analyze_data()

import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join("data", "youtube_trending.db")

def run_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def save_output(df, filename):
    output_path = os.path.join("data", filename)
    df.to_csv(output_path, index=False)
    print(f"Saved: {output_path}")

def perform_analysis():

    print("\nRunning full YouTube trending analytics...\n")

    # 1. Top 10 most viewed videos
    q1 = """
    SELECT title, channel, views
    FROM trending_videos
    ORDER BY views DESC
    LIMIT 10;
    """
    df1 = run_query(q1)
    save_output(df1, "top_10_most_viewed.csv")

    # 2. Top 10 most liked videos
    q2 = """
    SELECT title, channel, likes
    FROM trending_videos
    ORDER BY likes DESC
    LIMIT 10;
    """
    df2 = run_query(q2)
    save_output(df2, "top_10_most_liked.csv")

    # 3. Channels appearing most
    q3 = """
    SELECT channel, COUNT(*) AS total_count
    FROM trending_videos
    GROUP BY channel
    ORDER BY total_count DESC;
    """
    df3 = run_query(q3)
    save_output(df3, "channels_most_frequent.csv")

    # 4. Like-to-view engagement ratio
    q4 = """
    SELECT title, channel, views, likes,
           ROUND((likes * 1.0 / views) * 100, 2) AS engagement_percent
    FROM trending_videos
    ORDER BY engagement_percent DESC;
    """
    df4 = run_query(q4)
    save_output(df4, "engagement_scores.csv")

    print("\nAll analytics completed successfully!")

if __name__ == "__main__":
    perform_analysis()

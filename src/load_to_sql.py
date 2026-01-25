import sqlite3
import pandas as pd
import os

# Load transformed CSV path
transformed_file = os.path.join("data", "trending_data_transformed.csv")

def load_to_sql():
    # Read transformed data
    df = pd.read_csv(transformed_file)

    # Create or connect to database
    conn = sqlite3.connect(os.path.join("data", "youtube_trending.db"))

    # Load dataframe into SQL table
    df.to_sql("youtube_trending", conn, if_exists="replace", index=False)

    print("Data successfully loaded into SQLite database!")
    print("Database file created at: data/youtube_trending.db")

    conn.close()


if __name__ == "__main__":
    load_to_sql()

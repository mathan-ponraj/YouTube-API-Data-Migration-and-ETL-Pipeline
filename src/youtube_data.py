# src/youtube_data.py

from googleapiclient.discovery import build
import pandas as pd
import os
from config.config import API_KEY, REGION_CODE, MAX_RESULTS

def get_trending_videos(save_csv=True):
    """
    Fetch trending videos from YouTube API and save raw CSV if required.
    Returns a pandas DataFrame of raw video data.
    """
    # Build YouTube API client
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # Request most popular videos
    request = youtube.videos().list(
        part="snippet,statistics",
        chart="mostPopular",
        regionCode=REGION_CODE,
        maxResults=MAX_RESULTS
    )
    
    response = request.execute()
    
    # Extract relevant data
    video_data = []
    for item in response['items']:
        video_data.append({
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'views': item['statistics']['viewCount'],
            'likes': item['statistics'].get('likeCount', 0)
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(video_data)
    
    # Save raw CSV in project data folder
    if save_csv:
        raw_path = os.path.join('data', 'trending_data.csv')
        os.makedirs(os.path.dirname(raw_path), exist_ok=True)
        df.to_csv(raw_path, index=False)
        print(f"Raw data saved to {raw_path}")
    
    return df

def transform_data(df):
    """
    Clean and transform the raw DataFrame.
    Returns a transformed DataFrame.
    """
    df['views'] = df['views'].astype(int)
    df['likes'] = df['likes'].fillna(0).astype(int)
    df['channel'] = df['channel'].fillna('Unknown')
    df = df.drop_duplicates(subset=['title', 'channel'])
    
    # Reorder columns
    df = df[['title', 'channel', 'views', 'likes']]
    return df

def load_transformed_csv():
    """
    Load raw CSV from data folder, transform it, and save transformed CSV.
    Returns the transformed DataFrame.
    """
    raw_file = os.path.join('data', 'trending_data.csv')
    transformed_file = os.path.join('data', 'trending_data_transformed.csv')
    
    # Check if raw CSV exists
    if not os.path.exists(raw_file):
        print("Raw CSV not found. Please fetch data first using get_trending_videos().")
        return None
    
    # Load raw CSV
    df_raw = pd.read_csv(raw_file)
    
    # Transform data
    df_transformed = transform_data(df_raw)
    
    # Ensure folder exists and save transformed CSV
    os.makedirs(os.path.dirname(transformed_file), exist_ok=True)
    df_transformed.to_csv(transformed_file, index=False)
    print(f"Transformed data saved to {transformed_file}")
    
    return df_transformed

# Test script
if __name__ == "__main__":
    # Step 1: Fetch trending videos and save raw CSV
    df_trending = get_trending_videos(save_csv=True)
    print("Raw DataFrame:")
    print(df_trending.head(), "\n")
    
    # Step 2: Transform raw data and save transformed CSV
    df_clean = load_transformed_csv()
    if df_clean is not None:
        print("Transformed DataFrame:")
        print(df_clean.head())

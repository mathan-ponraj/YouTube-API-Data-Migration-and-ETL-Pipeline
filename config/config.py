# config/config.py

# Your YouTube Data API key
API_KEY = "AIzaSyAzeFsKSAtJBoS_ivAU7K7qTWTsq8UaxQ4"

DB_CONNECTION_STRING = "sqlite:///data/youtube_trending.db"

# Region code for trending videos
REGION_CODE = "IN"

# Maximum number of trending videos to fetch
MAX_RESULTS = 10
# config/config.py
import os

API_KEY = os.getenv("YT_API_KEY", "")  # set locally via .env or set in GitHub Secrets
REGION_CODE = os.getenv("REGION_CODE", "IN")
MAX_RESULTS = int(os.getenv("MAX_RESULTS", "10"))

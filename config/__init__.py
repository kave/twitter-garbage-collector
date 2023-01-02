import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, verbose=True)

# Twitter
CONSUMER_API_KEY = os.environ.get('CONSUMER_API_KEY')
CONSUMER_API_SECRET = os.environ.get('CONSUMER_API_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET_TOKEN = os.environ.get('ACCESS_SECRET_TOKEN')
TWITTER_USERNAME = os.environ.get('TWITTER_USERNAME')

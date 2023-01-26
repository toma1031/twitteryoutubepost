from apiclient.discovery import build
from apiclient.errors import HttpError
from requests_oauthlib import OAuth1Session
import settings
import random
import os

# API
YOUTUBE_API_KEY = os.environ['DEVELOPER_KEY']
DEVELOPER_KEY = YOUTUBE_API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY
    )

def get_video_by_random(video_channelId):

    search_response = youtube.search().list(
      part = "id",
      channelId = video_channelId,
      maxResults = 1000,
      type='video',
    ).execute()
    
    video_list = search_response

    # Value of item will be assigned to "items_value"
    items_value = video_list['items']

    # getting VideoID
    items_value_id_value = [items_value_id.get('id') for items_value_id in items_value]

    video_urls = [items_value_id_value_videoId.get('videoId') for items_value_id_value_videoId in items_value_id_value]

    # get URL by romdom
    choiced_url = random.choice(video_urls)
    
    return choiced_url



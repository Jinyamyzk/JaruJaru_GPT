import os
import json
import csv
from googleapiclient.discovery import build
from dotenv import load_dotenv
import datetime
from dateutil.relativedelta import relativedelta

load_dotenv()

# Youtube Data APIのキーを指定
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')

videos = [] #videoURLを格納する配列

def youtube_search(pagetoken, st, ed):
  youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

  search_response = youtube.search().list(
    channelId='UChwgNUWPM-ksOP3BbfQHS5Q',
    part='snippet',
    type='video',
    maxResults=50,
    publishedAfter=st,
    publishedBefore=ed, 
    pageToken=pagetoken
  ).execute()

  print(search_response["pageInfo"]["totalResults"])
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
        title = search_result["snippet"]["title"]
        id = search_result["id"]["videoId"]
        url = 'https://www.youtube.com/watch?v=%s' % search_result["id"]["videoId"]
        thumbnailUrl = search_result["snippet"]["thumbnails"]["default"]["url"]
        publishedAt = search_result["snippet"]["publishedAt"]
        videos.append([title, id, url, thumbnailUrl, publishedAt])


  try:
    nextPagetoken =  search_response["nextPageToken"] 
    youtube_search(nextPagetoken, st, ed)
  except:
    return

dt = datetime.datetime(2021, 2, 16, 0, 0)
for i in range(1, 12):
  print(dt.isoformat())
  youtube_search('', dt.isoformat()+'Z', (dt + relativedelta(months=1)).isoformat()+'Z')
  dt = dt + relativedelta(months=1)

with open("videolist.tsv", mode="a", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(videos)






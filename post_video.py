import settings, get_video
from requests_oauthlib import OAuth1Session

from post_video import twitter, url


def tweet_youtube_video2():
  tweetText = "Today's my art Video! https://www.youtube.com/watch?v=" + get_video.get_video_by_random('Write your Youtube Channel ID here')
  params = {'status' : tweetText}

  response = twitter.post(url, params = params)
  print(response.status_code)

if __name__ == "__main__":
  tweet_youtube_video2()

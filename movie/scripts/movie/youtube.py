import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def run():
    api = YoutubeAPI()
    result = api.all_search("悠木碧")
    print(result)

class YoutubeAPI:
    DEVELOPER_KEY = os.getenv("GOOGLE_DEVELOPER_KEY", "")
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    def __init__(self):
        self.client = build(
            self.YOUTUBE_API_SERVICE_NAME,
            self.YOUTUBE_API_VERSION,
            developerKey=self.DEVELOPER_KEY,
        )

    def all_search(self, keyword=''):
        return self.__search(keyword, max_results=50, order='date')

    def __search(self, keyword='', max_results=50, order='date'):
        result = self.client.search().list(
            q = keyword,
            part = 'id,snippet',
            maxResults = max_results,
            order = 'date',
            type = 'video',
        ).execute()

        return self.__parse(result)

    def __parse(self, response):
        youtubes = []
        for result in response.get('items', []):
            if result['id']['kind'] != 'youtube#video':
                continue
            y = Youtube(
                id = result['id']['videoId'],
                title = result['snippet']['title'],
                description = result['snippet']['description'],
                thumbnail = result['snippet']['thumbnails']['default'].get('url', ''),
            )
            youtubes.append(y)
        return youtubes



class Youtube:
    def __init__(self, id='', title='', description='', thumbnail=''):
        self.id = id,
        self.title = title,
        self.description = description
        self.thumbnail = thumbnail

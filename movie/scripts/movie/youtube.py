import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from movie.models.youtube import Youtube
from django.db.utils import IntegrityError


def run():
    api = YoutubeAPI()
    results = api.all_search("悠木碧")
    for result in results:
        try:
            result.save()
        except IntegrityError:
            print("Save error: %s" % result.__dict__.values())


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
            y = YoutubeMovie(
                result['id']['videoId'],
                title = result['snippet']['title'],
                description = result['snippet']['description'],
                thumbnail = result['snippet']['thumbnails']['default'].get('url', ''),
            )
            youtubes.append(y)
        return youtubes



class YoutubeMovie:
    def __init__(self, id, title='', description='', thumbnail=''):
        self.id = id
        self.url = "https://www.youtube.com/watch?v=" + str(self.id)
        self.title = title
        self.description = description
        self.thumbnail = thumbnail

    def __str__(self):
        self.id

    def save(self):
        y = Youtube(
            movie_id = self.id,
            title = self.title,
            description = self.description,
            url = self.url,
            thumbnail = self.thumbnail,
        )
        y.save()

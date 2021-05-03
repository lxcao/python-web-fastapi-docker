'''
Author: clingxin
Date: 2021-05-02 11:24:56
LastEditors: clingxin
LastEditTime: 2021-05-03 15:13:56
FilePath: /python-web-fastapi-docker/interface/movie_interface.py
'''
#from ..models.movie_model import MovieModel
#import models.movie_model as movieModel
from models.movie_model import MovieModel
from typing import Optional
import httpx

async def get_movie(title_subtext: str) -> Optional[MovieModel]:
    print(title_subtext)
    url = 'https://movieservice.talkpython.fm/api/search/' + title_subtext
    print(url)
    
    async with httpx.AsyncClient() as client:
        resp: httpx.Response = await client.get(url)
        print(resp)
        print(resp.status_code)
        print(resp.headers['content-type'])
        print(resp.text)
        resp.raise_for_status()
        data = resp.json()
    results = data['hits']
    if not results:
        return None
    movie = MovieModel(**results[0])
    return movie
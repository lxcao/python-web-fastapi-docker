'''
Author: clingxin
Date: 2021-05-01 18:24:41
LastEditors: clingxin
LastEditTime: 2021-05-03 15:53:18
FilePath: /python-web-fastapi-docker/service/movie_service.py
'''

import fastapi
from interfaces.movie_interface  import get_movie
from models.movie_model import MovieModel

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "message": "Hello world.",
        "usage": "Call /api/movie/{title} to use the API"
    }
    
@app.get('/api/movie/{title}', response_model=MovieModel)
async def movie_search(title: str):
    movie = await get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)
    return movie.dict()


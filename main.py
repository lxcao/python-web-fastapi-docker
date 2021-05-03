'''
Author: clingxin
Date: 2021-05-01 18:24:41
LastEditors: clingxin
LastEditTime: 2021-05-03 10:35:28
FilePath: /python-web-fastapi-docker/main.py
'''

import fastapi
import uvicorn
from service.movie_data import get_movie

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "message": "Hello world."
    }
    
@app.get('/api/movie/{title}')
async def movie_search(title: str):
    await get_movie(title)

if __name__ == '__main__':
    uvicorn.run(app)


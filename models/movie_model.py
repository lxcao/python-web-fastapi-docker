'''
Author: clingxin
Date: 2021-05-03 11:48:31
LastEditors: clingxin
LastEditTime: 2021-05-03 11:50:46
FilePath: /python-web-fastapi-docker/models/movie_model.py
'''

from typing import List
from pydantic import BaseModel

class MovieModel(BaseModel):
    title: str
    keywords: List[str] = []
    director: str
    year: int
'''
Author: clingxin
Date: 2021-05-03 15:49:55
LastEditors: clingxin
LastEditTime: 2021-05-04 14:41:41
FilePath: /python-web-fastapi-docker/main.py
'''
import uvicorn
from services.movie_service import app
# if __name__ == '__main__':
#     uvicorn.run(app)
uvicorn.run(app, host="0.0.0.0", port=8000)
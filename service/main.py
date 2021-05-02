'''
Author: clingxin
Date: 2021-05-01 18:24:41
LastEditors: clingxin
LastEditTime: 2021-05-02 08:10:15
FilePath: /python-web-fastapi-docker/service/main.py
'''

import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "message": "Hello world."
    }

if __name__ == '__main__':
    uvicorn.run(app)


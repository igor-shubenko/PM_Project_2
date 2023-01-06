import uvicorn
from fastapi import FastAPI


app = FastAPI(title='FastAPIHealthCheckServer',
              description="Server for healthchecks from AWS target group",
              version="1.0")

@app.get('/hello')
def hello():
    return {"Message": "Hi, i am healthy!"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8765, reload=True)

from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/hello')
def hello():
    return {"Message": "Hello students of PM group 1!"}



if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=1)


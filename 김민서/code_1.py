from fastapi import FastAPI

app = FastAPI()


@app.get('/hello') #: 행위 / 자원
def hello():
    return {'test': 'hello2'} #: 표현


@app.post('/users') #: 행위 / 자원
def create_user(username: str):
    return {'username': username}


@app.get('/users') #: 행위 / 자원
def create_user(username: str):
    return {'username': username}


@app.get('/users/{username}') #: 행위 / 자원
def create_user(username: str):
    return {'username': username}

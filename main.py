from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'data': 'home'}, 200
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

@app.get('/')
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {'username': credentials.username, 'password': credentials.password}

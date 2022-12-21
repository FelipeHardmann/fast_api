from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/')
def read_form():
    return 'Olá galera. Home-page para calcular o IMC em FastAPI!'

@app.get("/form")
def form_post(request: Request):
    result = 0
    return templates.TemplateResponse('form3.html', context={'request': request, 'result': result})

@app.post("/form")
def form_post(request: Request, peso: int = Form(...), altura: int = Form(...)):
    result = round((peso/((altura/100)**2)),1)
    return templates.TemplateResponse('form3.html', context={'request': request, 'result': result})

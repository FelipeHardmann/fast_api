from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = FastAPI()
# Aqui o Jinja2Templates está procurando o diretório chamado templates
templates = Jinja2Templates(directory = 'templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index5.html', context={'request': request})

@app.get("/form")
def form_post(request: Request):
    imc = 0.0
    return templates.TemplateResponse('form.html', context={'request': request, 'imc': imc})

@app.post("/form")
def form_post(request: Request, peso: int = Form(...), altura: int = Form(...)):
    imc = round((peso/((altura/100)**2)),1)
    return templates.TemplateResponse('form.html', context={'request': request, 'imc': imc})

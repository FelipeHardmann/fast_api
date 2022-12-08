from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
# Aqui o Jinja2Templates está procurando o diretório chamado templates
templates = Jinja2Templates(directory = 'templates')

@app.get('/')
def read_form():
    return 'Olá Estou construindo a home-page com FastAPI'

@app.get('/form')
def form_get(request: Request):
    result = ''
    return templates.TemplateResponse('form.html', context = {'request': request, 'result': result})

@app.post('/form')
def form_post(request: Request, num: int = Form(...)):
    result = (num)
    return templates.TemplateResponse('form.html', context = {'request': request, 'result': result})

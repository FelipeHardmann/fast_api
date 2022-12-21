from fastapi import FastAPI, Request, Form
from fastapi.templating import  Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')
comentarios = []

@app.get('/')
def read_form():
    return 'Construção de comentário Médico em FastAPI'

@app.get('/form')
def form_post(request: Request):
    return templates.TemplateResponse('form2.html', context={'request': request, 'comentarios': comentarios})

@app.post('/form')
def form_post(request: Request, text: str = Form(...)):
    comentarios.append(text)
    return templates.TemplateResponse('form2.html', context={'request': request, 'comentarios': comentarios})

@app.get('/comentarios')
def form_post(request: Request):
    return templates.TemplateResponse('form211.html', context={'request': request, 'comentarios': comentarios})


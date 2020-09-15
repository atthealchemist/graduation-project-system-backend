from datetime import datetime

from fastapi import APIRouter

main = APIRouter()


@main.get('/')
def home():
    return dict(hello='world')


@main.get('/time')
def time():
    return dict(now=str(datetime.now()))

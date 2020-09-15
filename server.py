import uvicorn
from fastapi import FastAPI

from server.utils import load_config
from server.routers import main_router, document_router

app = FastAPI()


def configure_app():
    app.include_router(main_router,
                       tags=['main'])
    app.include_router(document_router,
                       prefix='/documents',
                       tags=['document'])


def main():
    config = load_config()
    server = config['server']
    configure_app()
    uvicorn.run(app, host=server.get('host'), port=server.get('port'))


if __name__ == '__main__':
    main()

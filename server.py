from pathlib import Path

import uvicorn
from fastapi import FastAPI

from modules.database import init_database
from modules.routers import main_router, document_router, migration_router
from modules.utils import load_config

app = FastAPI()


def configure_app():
    app.include_router(main_router,
                       tags=['main'])
    app.include_router(document_router,
                       prefix='/documents',
                       tags=['document'])
    app.include_router(migration_router,
                       prefix='/migration',
                       tags=['migration'])


def main():
    server = load_config(section='modules')
    init_database()
    configure_app()
    uvicorn.run(app, host=server.get('host'), port=server.get('port'))


if __name__ == '__main__':
    main()

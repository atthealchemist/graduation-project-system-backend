import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.database import init_database
from modules.routers import *
from modules.utils import load_config

app = FastAPI()


def configure_app():
    origins = [
        "http://localhost:3999",
        "http://localhost:8000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(main_router,
                       tags=['main'])
    app.include_router(document_router,
                       prefix='/documents',
                       tags=['document'])
    app.include_router(user_router,
                       prefix='/users',
                       tags=['user'])
    app.include_router(space_router,
                       prefix='/spaces',
                       tags=['space'])
    app.include_router(migration_router,
                       prefix='/migration',
                       tags=['migration'])
    app.include_router(converter_router,
                       prefix='/converter',
                       tags=['converter'])
    app.include_router(publisher_router,
                       prefix='/publisher',
                       tags=['publisher'])


def main():
    server = load_config(section='server')
    init_database()
    configure_app()
    # "Thank you", uvloop! I should handle this stuff in cause of your Windows "support"!
    used_loop = 'asyncio' if 'win' in sys.platform else 'auto'
    uvicorn.run(app, host=server.get('host'), port=server.get('port'), loop=used_loop)


if __name__ == '__main__':
    main()

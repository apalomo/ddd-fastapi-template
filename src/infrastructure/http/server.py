from fastapi import FastAPI

from src.infrastructure.injections import Container
from src.infrastructure.http.user import router

def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.container = container
    app.include_router(router.router)
    return app


app = create_app()

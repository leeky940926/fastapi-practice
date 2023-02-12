from fastapi import FastAPI

from apps.albums.routers.albums import router as album_router
from apps.companies.routers.companies import router as company_router
from apps.singers.routers.singers import router as singer_router


def create_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.include_router(router=company_router)
    fastapi_app.include_router(router=singer_router)
    fastapi_app.include_router(router=album_router)
    return fastapi_app


app = create_app()


@app.get("/")
async def init_page():
    return {"message": "hihi"}

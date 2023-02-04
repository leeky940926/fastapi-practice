from fastapi import FastAPI

from apps.singers.routers import router


def create_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.include_router(router=router)
    return fastapi_app


app = create_app()


@app.get("/")
async def init_page():
    return {"message": "hihi"}

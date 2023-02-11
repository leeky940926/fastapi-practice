from fastapi import FastAPI

from apps.companies.routers.companies import router as company_router


def create_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.include_router(router=company_router)
    return fastapi_app


app = create_app()


@app.get("/")
async def init_page():
    return {"message": "hihi"}

from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from api.items import router as items_router
from api.users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"Hello:world"}


@app.get("/page_one/")
def another_page():
    return {
        "page_one": "That page number one!"
    }

@app.get("/ping/")
def another_page():
    return {
        "message": "pong"
    }


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    return JSONResponse(
        {
            "request url": request.url.path,
            "exception": str(exception),
        },
        status_code = status.HTTP_404_NOT_FOUND,
    )

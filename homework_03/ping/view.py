from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse


app = FastAPI()


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.exception_handler(status.HTTP_200_OK)
def ping(request, exception):
    return JSONResponse(
        {
        "request url": request.url.path,
        "exception": str(exception),
        },
        status_code=status.HTTP_200_OK
    )
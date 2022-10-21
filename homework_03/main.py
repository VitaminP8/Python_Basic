from urllib import response

from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse, Response

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ping/")
def view():
    return JSONResponse(
        {
            "message": Response(status_code=status.HTTP_200_OK),
        }
    )


@app.get("/{url_path:path}")
def all_other(url_path: str):
    return {"request to": url_path}

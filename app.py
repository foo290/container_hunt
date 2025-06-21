from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Mount static files at root
app.mount("/", StaticFiles(directory="static", html=True), name="static")



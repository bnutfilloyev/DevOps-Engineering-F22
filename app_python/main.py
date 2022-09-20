"""Develop and test a simple Python web application, that shows current time in Moscow."""
from fastapi import FastAPI
from datetime import datetime
from pytz import timezone
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    """Return current time in Moscow."""
    moscow = timezone('Europe/Moscow')
    return {"Moscow time": datetime.now(moscow).strftime("%H:%M:%S")}


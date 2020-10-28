from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import json
import uvicorn
import requests

app = FastAPI()

class Render_template:
    def __init__(self, templatename):
        self.template = templatename
    def renderhtml(self):
        with open(f"templates/{self.template}", "r") as index:
            return str(index.read())


@app.get("/", response_class=HTMLResponse)
async def root():
    index = Render_template("index.html")
    req = requests.get("http://localhost:6000/api")
    json_dict = json.dumps(req.json())
    resp = json_dict["nome-file"]
    return index.renderhtml()

@app.get("/api")
async def api():    
    return "ciao"


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=6000, reload=True)
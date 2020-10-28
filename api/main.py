from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import json

app = FastAPI()

class Render_template:
    def __init__(self, templatename):
        self.template = templatename
    def renderhtml(self):
        with open(f"templates/{self.template}", "r") as index:
            return str(index.read())
    def renderjson(self):
        with open(f"templates/{self.template}", "r") as index:
            return json.dumps(str(index.read()))

@app.get("/", response_class=HTMLResponse)
async def root():
    index = Render_template("index.html")
    return index.renderhtml()

@app.get("/api")
async def root():    
    return {"Hello World!": "ciao"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
import uvicorngit 
import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from logging import getLogger

logger = getLogger("uvicorn")

app = FastAPI()


@app.post("/")
async def index(request: Request):
    body = await request.json()
    logger.info(f"GET DATA:\n{json.dumps(body, indent=2, ensure_ascii=False)}")
    return JSONResponse(content=dict(msg="ok"), status_code=200)

if __name__ == '__main__':
    uvicorn.run("server:app", host="0.0.0.0", port=7071, log_level="info")

# pip install fastapi
# pip install uvicorn
# python server.py
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import util

app = FastAPI()

@app.api_route("/classify_image", methods=["GET", "POST"])
async def classify_image(image_data: str = Form(...)):
    result = util.classify_image(image_data)

    response = JSONResponse(content=result)
    response.headers["ACCESS-Control-Allow-Origin"] = "*"
    return response



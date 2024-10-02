from typing import Union

from fastapi import Body, FastAPI, HTTPException, Form
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from models import item
from db.session import engine

from routers import items

item.Base.metadata.create_all(bind=engine)

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = Field(
#         default=None, title="The description of the item", max_length=300
#     )
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: Union[float, None] = None


"""item: Annotated[Item, Body(embed=True)]
이 부분은 **item**이라는 파라미터가 Pydantic 모델인 Item의 인스턴스임을 나타냅니다. **Annotated**는 타입 힌트를 확장하는 방식으로 사용되며, FastAPI에서 추가적인 메타데이터를 제공하는 데 사용됩니다. Annotated를 통해 Item 모델을 더 구체적으로 설명하고 있습니다.

각 요소의 의미:
Annotated[Item, Body(embed=True)]:
Annotated는 Python 3.9 이상에서 사용 가능한 타입 힌트 확장 도구로, 타입에 메타데이터를 추가할 수 있습니다.
Item: 이 부분은 Pydantic 모델입니다. 즉, Item이라는 Pydantic 모델을 기반으로 한 객체가 들어오게 됩니다.
Body(embed=True): Body는 FastAPI에서 요청 본문을 처리하는 데 사용되는 클래스입니다. 여기서 embed=True 옵션을 사용하면, 요청 본문에서 item을 포함한 JSON 객체로 받습니다."""


# @app.post("/items/")
# async def update_item(item: Annotated[Item, Body(embed=True)]):
#     results = {"item": item}
#     return results

app.include_router(items.router, prefix="/item", tags=["item"])


@app.get("/{word}")
async def Home(word: str):
    return f"welcome {word}"


import requests

STABILITY_API_KEY = "sk-UufGozfi47kaelqpZAE0QlEFtI9bQc2e3QnWTevIb0TjUw6s"


@app.post("/generate-image/")
async def generate_image(
    prompt: str = Form(...),  # Required prompt field
    negative_prompt: str = Form(None),  # Optional negative prompt
    aspect_ratio: str = Form("1:1"),  # Optional aspect ratio with default 1:1
    seed: int = Form(0),  # Optional seed with default 0
    output_format: str = Form("png"),  # Optional output format, default is png
):
    # Stability AI endpoint
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

    # Prepare headers for the request
    headers = {
        "authorization": f"Bearer {STABILITY_API_KEY}",
        "accept": "image/*",  # Or application/json if you want the base64 image
    }

    # Data for the request
    data = {
        "prompt": prompt,
        "output_format": output_format,
        "aspect_ratio": aspect_ratio,
        "seed": seed,
    }

    # Include negative prompt if provided
    if negative_prompt:
        data["negative_prompt"] = negative_prompt

    try:
        # Sending the request to the Stability AI API
        response = requests.post(url, headers=headers, data=data, files={"none": ""})

        if response.status_code == 200:
            # Save the image to a file
            filename = f"./generated_image.{output_format}"
            with open(filename, "wb") as file:
                file.write(response.content)

            return {"message": f"Image successfully generated and saved as {filename}"}
        else:
            return {"error": response.json()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

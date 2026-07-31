from pydantic import BaseModel


class StoryCreate(BaseModel):
    title: str
    content: str


class StoryResponse(BaseModel):
    id: int
    title: str
    content: str

    model_config = {
        "from_attributes": True
    }
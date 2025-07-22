from typing import Dict, List, Any
from pydantic import BaseModel


class MemeModel(BaseModel):
    id: int
    info: Dict[str, object]
    tags: List[Any]
    text: str
    updated_by: str
    url: str


class DataContainerModel(BaseModel):
    data: List[MemeModel]

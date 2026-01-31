from pydantic import BaseModel, Field
from typing import List


class KeywordsRequest(BaseModel):
    article: str = Field(..., description="Wikipedia article title")
    depth: int = Field(0, ge=0, le=3, description="Traversal depth")
    ignore_list: List[str] = Field(default_factory=list)
    percentile: int = Field(0, ge=0, le=100, description="Percentile threshold for word counts")

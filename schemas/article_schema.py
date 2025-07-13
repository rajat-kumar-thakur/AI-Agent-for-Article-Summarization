from pydantic import BaseModel, Field
from typing import Optional, List

class EuronArticle(BaseModel):
    title: str = Field(..., description="Title of the article")
    articleUrl: str = Field(..., description="URL of the article")
    imageUrl: Optional[str] = Field(None, description="URL of the article's image")
    excerpt: Optional[str] = Field(None, description="Excerpt of the article")

class EuronArticleList(BaseModel):
    articles: List[EuronArticle] = Field(..., description="List of articles")
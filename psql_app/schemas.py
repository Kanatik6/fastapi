from datetime import datetime
from pydantic import BaseModel, Field


# Post, Put
class AuthorBase(BaseModel):
    first_name: str = Field(..., min_length=5, max_length=30)
    last_name: str = Field(..., min_length=5, max_length=30)

    class Config:
        orm_mode = True


#  return
class AuthorReturn(AuthorBase):
    id: int

    class Config:
        orm_mode = True


# Patch
class AuthorPatch(BaseModel):
    first_name: str | None = None
    last_name: str | None = None

    class Config:
        orm_mode = True


# ----
class PostBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=20)
    descriptions: str = Field(..., min_length=5)
    author_id: int 


# return
class PostReturn(PostBase):
    id: int
    likes: int
    unlikes: int
    date: datetime
    author_id: int
    author: AuthorReturn

    class Config:
        orm_mode = True


# Post
class PostCreate(PostBase):
    author_id: int 

    class Config:
        orm_mode = True


# Patch
class PostPatch(BaseModel):
    date: datetime = datetime.now()
    title: str | None = Field(None, min_length=5, max_length=20)
    descriptions: str | None = Field(None, min_length=5)

    class Config:
        orm_mode = True


# --------
class AuthorPostsReturn(AuthorReturn):
    posts: list[PostReturn] |None = None
    id: int

    class Config:
        orm_mode = True
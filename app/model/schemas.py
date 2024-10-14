
from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class PostFilterParams(BaseModel):
    # model_config = {"extra": "forbid"}
    title: Optional[str] = None
    status: Optional[str] = None
    include: Optional[str] = None

class PostBase(BaseModel):
    title: str
    content: str
    status: Optional[str]
    user_id: int

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]
    status: Optional[str]

class PostTags(BaseModel):
    tags: List[str]

class Post(PostBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    
class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user: Optional['User']
    tags: Optional[List['Tag']]
    comments: Optional[List['Comment']]

    @staticmethod
    def include_relations(obj, include):
        """Dynamically include relations based on 'include' query parameters"""
        if 'comments' not in include:
            obj.comments = []
        if 'tags' not in include:
            obj.tags = []
        if 'user' not in include:
            obj.user = None
        return obj
    
class UserBase(BaseModel):
    username: str
    email: str
    name: str
    
class UserCreate(UserBase):
    pass
class UserUpdate(BaseModel):
    name: Optional[str]

class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class UserResponse(UserBase):

    id: int
    posts: Optional[List['Post']] 
    comments: Optional[List['Comment']]

    @staticmethod
    def include_relations(obj, include: str):
        """Dynamically include relations based on 'include' query parameters"""    
        if 'comments' not in include:
            obj.comments = []
        if 'posts' not in include:
            obj.posts = []
        return obj
    
class TagBase(BaseModel):
    
    name: str

class TagCreate(TagBase):
    pass

class TagUpdate(BaseModel):
    name: str

class Tag(TagBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class CommentBase(BaseModel):
    content: str
    post_id: int
    user_id: int

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    content: str

class Comment(CommentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    post_id: int
    user_id: int

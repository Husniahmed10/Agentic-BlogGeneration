from typing import TypedDict 
from pydantic import BaseModel, Field 

class Blog(BaseModel):
    title:str=Field(description="The Title of the blog post")
    content:str=Field(description="The main content of the blog post")

class BlogState(TypedDict):
    topic:str # Topic of the blog
    blog:Blog # Blogs
    current_language:str # Current language of the blog

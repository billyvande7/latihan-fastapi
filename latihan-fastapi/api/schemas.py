from typing import Union
from pydantic import BaseModel

class Artist(BaseModel):
    name : str
    age : int
    gender : str

class Song(BaseModel):
    artist: Artist
    title : str
    duration : int

    class Config:
        orm_mode = True
# class RequestBook(BaseModel):
#     parameter : SongItem = Field(...)

class Token(BaseModel):
    access_token : str
    token_type : str

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None]  = None
    disabled: Union[bool, None]  = None

class UserInDB(User):
    hashed_password: str

class TokenData(BaseModel):
    username: Union[str, None] = None
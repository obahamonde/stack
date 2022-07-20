from sqlmodel import SQLModel
from pydantic import BaseModel, Field, EmailStr, HttpUrl, validator
from typing import Optional, List, Dict, Any, Union
from src.utils import id,now,avatar

class User(SQLModel, Table=True):
    id: str = Field(primary_key=True, default_factory=id)
    name : Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    picture: Optional[Union[HttpUrl,str]] = Field(default_factory=avatar)
from pydantic import HttpUrl, EmailStr, Field
from typing import Optional, List, Dict, Union
from src.lib.fql import Q
from src.utils import id as get_id, now as get_now , avatar as get_avatar


class User(Q):
    sub: str = Field(...)
    given_name: Optional[str] = Field()
    family_name: Optional[str] = Field()
    nickname: str = Field(...)
    name: Optional[str] = Field()
    picture: Optional[Union[HttpUrl,str]] = Field(default_factory=get_avatar)
    locale:Optional[str] = Field()
    updated_at :Optional[str] = Field()
    email: Optional[EmailStr] = Field()
    email_verified :Optional[bool] = Field()
    

class Account(User):
    email: EmailStr = Field(...)

class Media(Q):
    sub: str = Field(...)
    name: Optional[str] = Field()
    content_type: Optional[str] = Field()
    url: Optional[str] = Field()
    updated_at: Optional[float] = Field()
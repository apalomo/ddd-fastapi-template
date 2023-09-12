from pydantic import BaseModel
from pydantic import Field

class User(BaseModel):
    name: str = Field(description='Name of the user')
    fullname: str = Field(description='Full name of the user')
    nickname: str = Field(description='Nick Name of the user')


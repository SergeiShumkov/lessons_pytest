from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=2)

    # id: int
    title: str
    
    # name: str = Field(alias="_name") если переменная начинается с "_"

    # @validator("id")
    # def check_that_id_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError("Id is not less than two'")
    #     else:
    #         return v
# id, name, dep, age -> employee attributes
# in models we define the schema of the table for usage

from pydantic import BaseModel, Field, StrictInt
from typing import Optional
# in field(...) these 3 dots mean it is a required field
class Employee(BaseModel):
    id: int = Field(..., gt=0, title='Employee ID')
    name: str = Field(..., min_length=3, max_length=30)
    dep: str
    age: Optional[StrictInt] = Field(default=None, gt=21)
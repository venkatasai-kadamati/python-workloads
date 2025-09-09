# id, name, dep, age -> employee attributes
# in models we define the schema of the table for usage

from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    dep: str
    age: int
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# define a pydantic model for ease of validation
class User(BaseModel):
    id: int
    name: str

# response_model=User means that we are asking pydantic to play its role and validate as per the class definition of User
@app.get("/user", response_model=User)
def get_users():
    return User(id=1, name="sai")
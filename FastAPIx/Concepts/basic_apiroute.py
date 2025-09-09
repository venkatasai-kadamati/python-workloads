from fastapi import FastAPI

app = FastAPI()


# endpoint -> It is really easy.
# Just use decorator and set @app.<action>
@app.get("/")
def index():
    return {"message": "Hello, FastAPI! Application"}


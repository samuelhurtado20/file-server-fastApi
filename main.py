from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)


# uvicorn --help
# uvicorn main:app --host="0.0.0.0" --port="5000" --reload
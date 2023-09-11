from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.persons import app as user

import uvicorn

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
if __name__ == "__main__":
    uvicorn.run(app ="main:app", port=8000, reload=True)
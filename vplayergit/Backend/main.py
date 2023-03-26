from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.videos import video_router
from routers.server import server_router

app = FastAPI()
app.include_router(video_router)
app.include_router(server_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

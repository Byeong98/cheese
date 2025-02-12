from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.users import router as users_router

app = FastAPI()

# CORS 설정 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router.router)


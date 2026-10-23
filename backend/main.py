
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.auth import router as auth_router
from api.laundry import router as laundry_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend working"}

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(laundry_router, prefix="/laundry", tags=["Laundry"])

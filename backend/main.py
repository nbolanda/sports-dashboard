from fastapi import FastAPI
from app.routes import stats

app = FastAPI()
app.include_router(stats.router)

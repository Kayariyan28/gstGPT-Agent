from fastapi import FastAPI
from app.core.config import settings

from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
# Import models to register them with Base
from app.models import invoice, return_filing

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="gstGPT API",
    description="Backend API for gstGPT - AI GST Counsel & Filing Agent",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers import invoices, returns, chat

app.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
app.include_router(returns.router, prefix="/returns", tags=["returns"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])

@app.get("/health")
async def health_check():
    return {"status": "ok", "app_name": settings.PROJECT_NAME}

@app.get("/")
async def root():
    return {"message": "Welcome to gstGPT API"}

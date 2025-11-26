from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "gstGPT"
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5433/gstgpt"
    GEMINI_API_KEY: str = "mock-key"
    OPENAI_API_KEY: str = "mock-key"
    
    class Config:
        env_file = ".env"

settings = Settings()

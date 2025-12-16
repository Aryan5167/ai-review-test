from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Code Reviewer"
    APP_ENV: str = "dev"

    DATABASE_URL: str
    # LLM
    LLM_PROVIDER: str 
    GROQ_API_KEY: str | None = None
    OPENAI_API_KEY: str | None = None
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    # GitHub Webhook
    WEBHOOK_SECRET: str | None = None
    GITHUB_TOKEN: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

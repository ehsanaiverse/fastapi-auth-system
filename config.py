from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings"""
    
    SECRET_KEY: str = "default-secret-key-please-change"
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "postgresql://neondb_owner:npg_JuQciI1Y9eTg@ep-crimson-sound-advvvxil-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings():
    """Get cached settings instance"""
    return Settings()


# Create a global settings instance
settings = get_settings()
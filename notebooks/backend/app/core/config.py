from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "RAG Application"
    DEBUG: bool = True


settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # app_name: str = "Bookly APIs"
    # admin_email: str
    # items_per_user: int = 50
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore",
        env_file_encoding="utf-8"
        )


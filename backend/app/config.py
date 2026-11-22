from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

APP_VERSION = "0.1.0"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # LLM
    llm_provider: str = "anthropic"
    anthropic_api_key: str = ""
    llm_model: str = "claude-sonnet-5-5"
    llm_max_tokens: int = 4096

    # App
    default_region: str = "eu-west-3"
    database_path: str = "/data/archi.db"
    enable_tf_fmt: bool = True
    cors_origins: str = ""

    @property
    def chat_enabled(self) -> bool:
        return self.llm_provider == "anthropic" and bool(self.anthropic_api_key.strip())

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()

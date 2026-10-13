import os
from functools import lru_cache
from pathlib import Path
from dotenv import load_dotenv

# Search explicit .env locations
possible_env_paths = [
    Path(__file__).resolve().parents[2] / ".env",  # backend/.env
    Path(__file__).resolve().parents[3] / ".env",  # root/.env
    Path.cwd() / ".env",
    Path.cwd() / "backend" / ".env"
]
for _p in possible_env_paths:
    if _p.exists():
        load_dotenv(dotenv_path=_p, override=False)

class Settings:
    _raw_url: str = os.getenv("SUPABASE_URL", "").strip()
    # Normalize URL: strip trailing /rest/v1/ or trailing slash
    SUPABASE_URL: str = (
        _raw_url.replace("/rest/v1/", "").replace("/rest/v1", "").rstrip("/")
        if _raw_url else ""
    )
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "").strip()
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "").strip()
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "").strip()
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

@lru_cache()
def get_settings() -> Settings:
    """Returns cached instance of application settings."""
    return Settings()


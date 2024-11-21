from decouple import config

class Settings:
    POSTGRES_USER = config("POSTGRES_USER", default="postgres")
    POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", default="password")
    POSTGRES_DB = config("POSTGRES_DB", default="database")
    POSTGRES_HOST = config("POSTGRES_HOST", default="localhost")
    POSTGRES_PORT = config("POSTGRES_PORT", default="5432")

    DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

settings = Settings()
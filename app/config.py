from pydantic import Field, PostgresDsn, computed_field
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    model_config = {"env_prefix": "DATABASE_"}

    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    NAME: str


class Settings(BaseSettings):
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql",
                username=self.database.USER,
                password=self.database.PASSWORD,
                host=self.database.HOST,
                port=self.database.PORT,
                path=self.database.NAME,
            )
        )


settings = Settings()

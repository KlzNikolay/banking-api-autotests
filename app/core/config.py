from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс с настройками проекта.

    Значения берутся из переменных окружения или из файла .env.
    Если обязательной переменной нет — приложение упадет при старте
    с понятной ошибкой валидации.
    """

    db_host_1: str
    db_host_2: str

    db_name: str
    db_port: int
    db_user: str
    db_password: str

    api_base_url: str

    # Говорим Pydantic, что настройки нужно читать из файла .env.
    # extra="ignore" означает: если в .env появятся лишние переменные,
    # не падать с ошибкой.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# Создаем единый объект настроек, который будем импортировать в других файлах.
settings = Settings()

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings


# Собираем строку подключения к PostgreSQL из настроек.
# Значения берутся не из кода, а из .env через settings.
DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{settings.db_user}:"
    f"{settings.db_password}@"
    f"{settings.db_host_1}:"
    f"{settings.db_port}/"
    f"{settings.db_name}"
)

# engine — объект SQLAlchemy, через который выполняется подключение к БД.
engine = create_engine(DATABASE_URL)

# SessionLocal создает сессии для работы с БД.
# Через сессию мы будем делать query, add, commit и т.д.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base — базовый класс для ORM-моделей.
# Все модели таблиц будут наследоваться от него.
Base = declarative_base()
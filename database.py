from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


async_engine = create_async_engine('sqlite+aiosqlite:///tasks.db')
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


# Описание модели
class TasksOrm(Model):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


# Создание таблиц моделей в базе данных асинхронно
async def create_tables_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


# Удаление таблиц моделей в базе данных асинхронно
async def drop_tables_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

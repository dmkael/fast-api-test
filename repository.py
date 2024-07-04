from sqlalchemy import select

from database import async_session, TasksOrm
from schemas import SchTaskAdd, SchTaskGet


class TaskRepository:
    @classmethod
    async def add_one(cls, data: SchTaskAdd) -> int:
        async with async_session() as session:
            task_dict = data.model_dump()
            # Распаковка аргументов и формирование объекта модели
            task = TasksOrm(**task_dict)
            session.add(task)
            # Отправка изменений в базу данных и получение id объекта в базе данных (аналог RETURNING?)
            await session.flush()
            # Сохранение изменений в базе данных
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[SchTaskGet] or None:
        async with async_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            tasks = result.scalars().all()
            print(tasks)
            if tasks is None:
                return
            tasks_schema = [SchTaskGet.model_validate(task) for task in tasks]
            print(tasks_schema)
            return tasks_schema

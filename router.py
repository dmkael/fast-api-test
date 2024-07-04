from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import SchTaskAdd, SchTaskGet, SchTaskResponse
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post("/")
async def post_task(task: Annotated[SchTaskAdd, Depends()]) -> SchTaskResponse:
    task_id = await TaskRepository.add_one(task)
    return SchTaskResponse(task_id=task_id)


@router.get("/")
async def get_tasks() -> list[SchTaskGet]:
    tasks = await TaskRepository.get_all()
    return tasks

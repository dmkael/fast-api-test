from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables_db, drop_tables_db
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting lifespan")
    # await drop_tables_db()
    # print("Database dropped")
    # await create_tables_db()
    # print("Database created")
    yield
    print("Stopping lifespan")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

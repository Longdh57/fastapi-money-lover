import uvicorn
import logging
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.api.api import router
from app.core.config import settings
from app.models.base_model import Base
from app.db.base_class import engine
from app.utils.exception import AppBaseException, base_exception_handler

logging.config.fileConfig(settings.LOGGING_CONFIG_FILE, disable_existing_loggers=False)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_PREFIX}/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=settings.API_PREFIX)
app.add_exception_handler(AppBaseException, base_exception_handler)
app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

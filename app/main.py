import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api import router
from app.core.config import settings
from app.db.base_class import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_PREFIX}/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.include_router(router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

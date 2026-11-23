from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

# Create an asynchronous SQLAlchemy engine using the database URL from settings
engine = create_async_engine(settings.database_url)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    """
    Dependency that provides a database session for use in FastAPI routes.
    It creates a new session for each request and ensures it is closed after use.
    """
    async with SessionLocal() as session:
        yield session
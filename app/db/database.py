from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.db.data import employers_data, jobs_data
from app.db.models import Base, Employer, Job
from app.settings.config import DB_URL

# an engine is a factory for connections
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)


def prepare_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = SessionLocal()

    for employer in employers_data:
        session.add(Employer(**employer))

    for job in jobs_data:
        session.add(Job(**job))

    session.commit()
    session.close()


def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

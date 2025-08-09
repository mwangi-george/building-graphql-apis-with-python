from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.data import employers_data, jobs_data, users_data, job_applications_data
from app.db.models import Base, Employer, Job, User, JobApplication
from app.settings.config import DB_URL
from app.utils import hash_password

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

    for user in users_data:
        user["password"] = hash_password(user["password"])
        session.add(User(**user))

    for job_application in job_applications_data:
        session.add(JobApplication(**job_application))

    session.commit()
    session.close()

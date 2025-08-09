from graphene import Mutation, String, Field, Int, Boolean
from sqlalchemy.exc import IntegrityError
from loguru import logger

from app.db.database import SessionLocal
from app.db.models import JobApplication
from app.gql.types import JobApplicationObject
from app.utils import logged_in_user, admin_user


class AddJobApplication(Mutation):
    class Arguments:
        job_id = Int(required=True)
        user_id = Int(required=True)

    job_application = Field(lambda: JobApplicationObject)

    @staticmethod
    @logged_in_user
    def mutate(root, info, job_id, user_id):
        with SessionLocal() as session:
            job_application = session.query(JobApplication).filter_by(job_id=job_id, user_id=user_id).first()
            if job_application:
                raise Exception("Job application already exists")
            job_application = JobApplication(job_id=job_id, user_id=user_id)
            session.add(job_application)
            try:
                session.commit()
                session.refresh(job_application)
                return AddJobApplication(job_application=job_application)
            except IntegrityError as e:
                logger.error(f"IntegrityError: {str(e)}")
                session.rollback()
                raise Exception("Invalid job id or user id")


class DeleteJobApplication(Mutation):
    class Arguments:
        application_id = Int(required=True)

    success = Boolean()

    @staticmethod
    @admin_user
    def mutate(root, info, application_id):
        with SessionLocal() as session:
            job_application = session.query(JobApplication).filter_by(id=application_id).first()
            if not job_application:
                raise Exception("Job application does not exist")
            session.delete(job_application)
            session.commit()
            return DeleteJobApplication(success=True)
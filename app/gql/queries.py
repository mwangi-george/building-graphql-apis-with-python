from graphene import ObjectType, List, Field, Int

from app.db.database import SessionLocal
from app.db.models import Employer, Job, User, JobApplication
from app.gql.types import EmployerObject, JobObject, UserObject, JobApplicationObject


class Query(ObjectType):
    employer = Field(EmployerObject, employer_id=Int(required=True))
    employers = List(EmployerObject)

    job = Field(JobObject, job_id=Int(required=True))
    jobs = List(JobObject)

    user = Field(UserObject, user_id=Int(required=True))
    users = List(UserObject)

    job_application = Field(JobApplicationObject, job_id=Int(required=True), user_id=Int(required=True))
    job_applications = List(JobApplicationObject)

    @staticmethod
    def resolve_employer(root, info, employer_id):
        with SessionLocal() as session:
            return session.query(Employer).filter_by(id=employer_id).first()

    @staticmethod
    def resolve_employers(root, info):
        with SessionLocal() as session:
            return session.query(Employer).all()

    @staticmethod
    def resolve_job(root, info, job_id):
        with SessionLocal() as session:
            return session.query(Job).filter(Job.id == job_id).first()

    @staticmethod
    def resolve_jobs(root, info):
        with SessionLocal() as session:
            return session.query(Job).all()

    @staticmethod
    def resolve_user(root, info, user_id):
        with SessionLocal() as session:
            return session.query(User).filter_by(id=user_id).first()

    @staticmethod
    def resolve_users(root, info):
        with SessionLocal() as session:
            return session.query(User).all()

    @staticmethod
    def resolve_job_application(root, info, job_id, user_id):
        with SessionLocal() as session:
            return session.query(JobApplication).filter_by(job_id=job_id, user_id=user_id).first()

    @staticmethod
    def resolve_job_applications(root, info):
        with SessionLocal() as session:
            return session.query(JobApplication).all()

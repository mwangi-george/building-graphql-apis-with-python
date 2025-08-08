from graphene import ObjectType, List

from sqlalchemy.orm import joinedload
from app.db.database import SessionLocal
from app.db.models import Employer, Job
from app.gql.types import EmployerObject, JobObject


def get_employers():
    with SessionLocal() as session:
        return session.query(Employer).options(joinedload(Employer.jobs)).all()

def get_jobs():
    with SessionLocal() as session:
        return session.query(Job).options(joinedload(Job.employer)).all()


class Query(ObjectType):
    employers = List(EmployerObject)
    jobs = List(JobObject)

    @staticmethod
    def resolve_employers(root, info):
        return get_employers()

    @staticmethod
    def resolve_jobs(root, info):
        return get_jobs()
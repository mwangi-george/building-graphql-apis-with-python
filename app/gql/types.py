from graphene import ObjectType, String, List, Field
from app.db.data import employers_data, jobs_data

class EmployerObject(ObjectType):
    id = String()
    name = String()
    contact_email = String()
    industry = String()
    jobs = List(lambda: JobObject)

    @staticmethod
    def resolve_jobs(root, info):
        return root.jobs


class JobObject(ObjectType):
    id = String()
    title = String()
    description = String()
    employer_id = String()
    employer = Field(lambda: EmployerObject)

    @staticmethod
    def resolve_employer(root, info):
        return root.employer

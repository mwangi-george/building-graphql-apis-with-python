from graphene import ObjectType, String, List, Field, DateTime


class EmployerObject(ObjectType):
    id = String()
    name = String()
    contact_email = String()
    industry = String()
    created_at = DateTime()
    jobs = List(lambda: JobObject)

    @staticmethod
    def resolve_jobs(root, info):
        return root.jobs


class JobObject(ObjectType):
    id = String()
    title = String()
    description = String()
    employer_id = String()
    created_at = DateTime()
    employer = Field(lambda: EmployerObject)

    @staticmethod
    def resolve_employer(root, info):
        return root.employer


class UserObject(ObjectType):
    id = String()
    username = String()
    email = String()
    role = String()
    created_at = DateTime()


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
    job_applications = List(lambda: JobApplicationObject)

    @staticmethod
    def resolve_job_applications(root, info):
        return root.job_applications

    @staticmethod
    def resolve_employer(root, info):
        return root.employer


class UserObject(ObjectType):
    id = String()
    username = String()
    email = String()
    role = String()
    created_at = DateTime()
    job_applications = List(lambda: JobApplicationObject)

    @staticmethod
    def resolve_job_applications(root, info):
        return root.job_applications


class JobApplicationObject(ObjectType):
    id = String()
    job_id = String()
    user_id = String()
    created_at = DateTime()
    job = Field(lambda: JobObject)
    user = Field(lambda: UserObject)

    @staticmethod
    def resolve_job(root, info):
        return root.job

    @staticmethod
    def resolve_user(root, info):
        return root.user

from graphene import ObjectType
from app.gql.employer.mutations import AddEmployer, UpdateEmployer, DeleteEmployer
from app.gql.job.mutations import AddJob, UpdateJob, DeleteJob
from app.gql.user.mutations import AddUser, UpdateUser, DeleteUser, LoginUser
from app.gql.job_application.mutations import AddJobApplication, DeleteJobApplication



class Mutation(ObjectType):
    add_job = AddJob.Field()
    update_job = UpdateJob.Field()
    delete_job = DeleteJob.Field()

    add_employer = AddEmployer.Field()
    update_employer = UpdateEmployer.Field()
    delete_employer = DeleteEmployer.Field()

    add_user = AddUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    add_job_application = AddJobApplication.Field()
    delete_job_application = DeleteJobApplication.Field()
    login_user = LoginUser.Field()
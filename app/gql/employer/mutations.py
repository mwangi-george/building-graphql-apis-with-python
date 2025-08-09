from graphene import Mutation, String, Field, Int

from app.db.database import SessionLocal
from app.db.models import Employer
from app.gql.types import EmployerObject
from app.utils import admin_user


class AddEmployer(Mutation):
    class Arguments:
        name = String(required=True)
        contact_email = String(required=True)
        industry = String(required=True)

    employer = Field(lambda: EmployerObject)

    @staticmethod
    @admin_user
    def mutate(root, info, name, contact_email, industry):
        employer = Employer(name=name, contact_email=contact_email, industry=industry)
        with SessionLocal() as session:
            session.add(employer)
            session.commit()
            session.refresh(employer)
        return AddEmployer(employer=employer)


class UpdateEmployer(Mutation):
    class Arguments:
        employer_id = Int(required=True)
        name = String()
        contact_email = String()
        industry = String()

    employer = Field(lambda: EmployerObject)

    @staticmethod
    @admin_user
    def mutate(root, info, employer_id, name=None, contact_email=None, industry=None):
        session = SessionLocal()
        employer = session.query(Employer).filter_by(id=employer_id).first()

        if not employer:
            raise Exception("Employer not found")

        if name:
            employer.name = name
        if contact_email:
            employer.contact_email = contact_email
        if industry:
            employer.industry = industry

        session.commit()
        session.refresh(employer)
        return UpdateEmployer(employer=employer)


class DeleteEmployer(Mutation):
    class Arguments:
        employer_id = Int(required=True)

    employer = Field(lambda: EmployerObject)

    @staticmethod
    @admin_user
    def mutate(root, info, employer_id):
        session = SessionLocal()
        employer = session.query(Employer).filter_by(id=employer_id).first()
        if not employer:
            raise Exception("Employer not found")
        session.delete(employer)
        session.commit()
        return DeleteEmployer(employer=employer)

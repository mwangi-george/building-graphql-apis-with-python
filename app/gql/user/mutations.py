from graphene import Mutation, String, Field, Int, Boolean
from sqlalchemy.exc import IntegrityError
from loguru import logger

from app.db.database import SessionLocal
from app.db.models import User
from app.gql.types import UserObject


class AddUser(Mutation):
    class Arguments:
        username = String(required=True)
        email = String(required=True)
        password = String(required=True)
        role = String(required=True)

    user = Field(lambda: UserObject)

    @staticmethod
    def mutate(root, info, username, email, password, role):
        session = SessionLocal()

        user = User(username=username, email=email, password=password, role=role)
        session.add(user)
        try:
            session.commit()
            session.refresh(user)
            return AddUser(user=user)
        except IntegrityError as e:
            logger.error(f"IntegrityError: {str(e)}")
            session.rollback()
            raise Exception("Username or email already exists")


class UpdateUser(Mutation):
    class Arguments:
        user_id = Int(required=True)
        username = String()
        email = String()
        password = String()
        role = String()

    user = Field(lambda: UserObject)

    @staticmethod
    def mutate(root, info, user_id, username=None, email=None, password=None, role=None):
        session = SessionLocal()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            raise Exception("User not found")

        if username:
            user.username = username

        if email:
            user.email = email

        if password:
            user.password = password

        if role:
            user.role = role

        session.commit()
        session.refresh(user)
        return UpdateUser(user=user)


class DeleteUser(Mutation):
    class Arguments:
        user_id = Int(required=True)

    success = Boolean()

    @staticmethod
    def mutate(root, info, user_id):
        session = SessionLocal()
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            raise Exception("User not found")
        session.delete(user)
        session.commit()
        return DeleteUser(success=True)


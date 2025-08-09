from contextlib import asynccontextmanager

from fastapi import FastAPI
from graphene import Schema
from starlette_graphene3 import GraphQLApp, make_playground_handler

from app.db.database import prepare_database
from app.gql.mutations import Mutation
from app.gql.queries import Query

schema = Schema(query=Query, mutation=Mutation)


# prepare database on startup
@asynccontextmanager
async def lifespan(app_instance: FastAPI):
    # startup action
    print("Starting up...")
    prepare_database()
    yield
    # shutdown action
    print("Shutting down...")


app = FastAPI(
    title="GraphQL API",
    description="GraphQL API",
    lifespan=lifespan,
)

app.mount(
    path="/",
    app=GraphQLApp(
        schema=schema,
        on_get=make_playground_handler()
    )
)
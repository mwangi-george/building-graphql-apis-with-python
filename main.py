from graphene import Schema, ObjectType, String
from loguru import logger


# Root Class of the schema
class Query(ObjectType):
    hello = String(name=String(default_value="world"))

    # resolver function: responsible for fetching and returning the data for a particular field
    def resolve_hello(self, info, name):
        logger.info(f"Resolving hello for name: {name}")
        return f"Hello, {name}!"

# instance of the Schema
schema = Schema(query=Query)


# query document
gql = """
{
    hello(name: "GraphQL")
}
"""

if __name__ == '__main__':
    result = schema.execute(gql)
    print(result)

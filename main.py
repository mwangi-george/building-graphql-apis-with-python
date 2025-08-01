from typing import Any

from graphene import (
    Schema, ObjectType, String, Int, Boolean, Field, List, Mutation,
)


class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()
    is_active = Boolean()


# Root Class of the schema
class Query(ObjectType):
    user = Field(UserType, user_id=Int())
    users_by_min_age = List(UserType, min_age=Int())

    # dummy data store
    users = [
        {"id": 1, "name": "John", "age": 18, "is_active": True},
        {"id": 2, "name": "Dave", "age": 28, "is_active": True},
        {"id": 3, "name": "Ken", "age": 13, "is_active": False},
        {"id": 4, "name": "Mark", "age": 48, "is_active": True},
    ]

    @staticmethod
    def resolve_user(root, info, user_id) -> dict[str, Any]:
        matched_users = [user for user in Query.users if user["id"] == user_id]
        return matched_users[0] if matched_users else None

    @staticmethod
    def resolve_users_by_min_age(root, info, min_age) -> list[dict[str, Any]]:
        return [user for user in Query.users if user["age"] >= min_age]


# Mutation
class CreateUser(Mutation):

    # inputs arguments for the mutation
    class Arguments:
        name = String()
        age = Int()

    # output type
    user = Field(UserType)

    # mutation handling
    @staticmethod
    def mutate(root, info, name, age):
        user = {"id": len(Query.users) + 1, "name": name, "age": age, "is_active": False}
        Query.users.append(user)
        return CreateUser(user=user)

class Mutation(ObjectType):
    create_user = CreateUser.Field()

# instance of the Schema
schema = Schema(query=Query, mutation=Mutation)


# query document
gql = """
query getUserById {
    user(userId: 5) {
        id
        name
        isActive
    }
}

# query getUsersByMinAge {
#     usersByMinAge(minAge: 48) {
#         id
#         name
#         age
#     }
# }
"""

gql_mutation = """
mutation {
    createUser(name: "Marvin", age: 18) {
        user {
            name
            isActive
        }
    }
}   
"""

if __name__ == '__main__':
    result = schema.execute(gql_mutation)
    print(result)
    result = schema.execute(gql)
    print(result)

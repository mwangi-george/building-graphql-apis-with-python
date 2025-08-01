from graphene import Schema, ObjectType, String, Int, Boolean, Field


class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()
    is_active = Boolean()


# Root Class of the schema
class Query(ObjectType):
    user = Field(UserType, user_id=Int())

    # dummy data store
    users = [
        {"id": 1, "name": "John", "age": 18, "is_active": True},
        {"id": 2, "name": "Dave", "age": 28, "is_active": True},
        {"id": 3, "name": "Ken", "age": 13, "is_active": False},
        {"id": 4, "name": "Mark", "age": 48, "is_active": True},
    ]

    def resolve_user(self, info, user_id):
        print(Query.users)
        matched_users = [user for user in Query.users if user["id"] == user_id]
        return matched_users[0] if matched_users else None

# instance of the Schema
schema = Schema(query=Query)


# query document
gql = """
query getUserById {
    user(userId: 1) {
        # age
        isActive
    }
}
"""

if __name__ == '__main__':
    result = schema.execute(gql)
    print(result)

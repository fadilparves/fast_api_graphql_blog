import graphene
from serializers import (
    UserGrapheneInputModel,
    UserGrapheneModel,
    PostGrapheneInputModel,
    PostGrapheneModel,
    CommentGrapheneInputModel,
    CommentGrapheneModel,
)
from models.comment import Comments
from models.post import Post
from models.user import User

class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))

    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f'Hello {name}'

class CreateUser(graphene.Mutation):
    class Arguments:
        user_details = UserGrapheneInputModel()

    Output = UserGrapheneModel

    @staticmethod
    def mutate(parent, info, user_details):
        user = User()
        user.name = user_details.name
        user.address = user_details.address
        user.phone_number = user_details.phone_number
        user.sex = user_details.sex

        user.save()

        return user
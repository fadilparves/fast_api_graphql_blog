from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp
from schema import Query, Mutation
from models.user import User

app = FastAPI()

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))

@app.get('/')
def home():
    return {'data': 'home'}, 200
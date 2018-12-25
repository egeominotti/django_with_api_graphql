from graphene_django import DjangoObjectType
import graphene
from testing.models import Utente

class User(DjangoObjectType):
    class Meta:
        model =Utente

class Query(graphene.ObjectType):

    users = graphene.List(User)

    print(users)

    def resolve_users(self, info):
        return Utente.objects.all()

schema = graphene.Schema(query=Query)
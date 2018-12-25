from graphene_django import DjangoObjectType
import graphene
from graphene_django.filter import DjangoFilterConnectionField

from testing.models import Utente,Post

'''
https://docs.graphene-python.org/en/latest/types/mutations/
https://docs.graphene-python.org/projects/django/en/latest/filtering/
'''

class User(DjangoObjectType):

    class Meta:
        model = Utente
        filter_fields = {'id','nome'}
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):

    users =         graphene.relay.Node.Field(User)
    all_users =     DjangoFilterConnectionField(User)


schema = graphene.Schema(query=Query)
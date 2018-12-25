import graphene
from django.http import HttpResponse
from django.shortcuts import render


class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')

    def resolve_hello(self, info):
        return 'World'

schema = graphene.Schema(query=Query)

def home(request):
    return render(request,'home.html')

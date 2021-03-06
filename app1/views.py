from django.shortcuts import render
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (filters, generics, permissions, renderers, response, schemas, viewsets)
from rest_framework.decorators import api_view, action, renderer_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
#from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRendererfrom 
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from app1.permissions import IsOwnerOrReadOnly
from app1.serializers import *
from .models import *
import calendar 
import time
import requests
# Create your views here.

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])

def schema_view(request):
    generator = schemas.SchemaGenerator(title='Rest API')
    return response.Response(generator.get_schema(request=request))

def index(request):
     return HttpResponse("Rest API")

class EmployeeTableList(viewsets.ModelViewSet):
    """
    This Employee Records rest api allows Get, Post, Delete, Put, Patch actions.
    """
    queryset = EmployeeTable.objects.all()    
    serializer_class = EmployeeTableSerializer


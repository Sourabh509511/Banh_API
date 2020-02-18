from django.shortcuts import render
from rest_framework import viewsets
from .models import Bank,Branch
from .serializers import Bankserializers,Branchesserializers
from django_filters.rest_framework import DjangoFilterBackend

class bankviewsets(viewsets.ModelViewSet):
    queryset=Bank.objects.all()
    serializer_class=Bankserializers

class branchviewsets(viewsets.ModelViewSet):
    queryset=Branch.objects.all()
    serializer_class=Branchesserializers
    filter_backends=(DjangoFilterBackend,)
    filter_fields=('ifsc','bank_name','city')

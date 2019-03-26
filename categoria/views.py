# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import Categoria
from .serializers import CategoriaSerializer


class CategoriaListView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

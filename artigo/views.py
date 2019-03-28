# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Artigo
from .serializers import ArtigoSerializer


class Pagination(PageNumberPagination):
    page_size = 3


class ArtigosListView(generics.ListAPIView):
    serializer_class = ArtigoSerializer
    pagination_class = Pagination

    def get_queryset(self):
        queryset = Artigo.objects.all()
        autor = self.request.query_params.get('autor', None)
        if autor:
            queryset = queryset.filter(autor__nome=autor)
        categoria = self.request.query_params.get('categoria', None)
        if categoria:
            queryset = queryset.filter(categorias__id=categoria)
        conteudo = self.request.query_params.get('conteudo', None)
        queryset = queryset.order_by('-data_criacao')
        return queryset


class ArtigosCreateView(generics.CreateAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer


class ArtigoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer

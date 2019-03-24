# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import Artigo
from .serializers import ArtigoSerializer


class ArtigosListView(generics.ListCreateAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer


class ArtigoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer

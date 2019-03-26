# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Artigo, Autor
from categoria.serializers import CategoriaSerializer


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = '__all__'


class ArtigoSerializer(serializers.ModelSerializer):

    categorias = CategoriaSerializer(read_only=True, many=True)
    autor = AutorSerializer(read_only=True)
    data_criacao = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S")
    ultima_modificacao = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S")

    class Meta:
        model = Artigo
        fields = ('id', 'titulo', 'conteudo', 'autor', 'categorias', 'data_criacao',
                  'ultima_modificacao', 'publicado')

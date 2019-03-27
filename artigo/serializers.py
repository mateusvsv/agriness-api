# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Artigo, Autor
from categoria.serializers import CategoriaSerializer
from categoria.models import Categoria


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ('id', 'nome', 'email')


class ArtigoSerializer(serializers.ModelSerializer):

    categorias = CategoriaSerializer(many=True)
    autor = AutorSerializer()
    data_criacao = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", required=False)
    ultima_modificacao = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S", required=False)

    class Meta:
        model = Artigo
        fields = ('id', 'titulo', 'conteudo', 'autor', 'categorias', 'data_criacao',
                  'ultima_modificacao', 'publicado')

    def create(self, validated_data):
        autor = Autor(**validated_data.pop('autor'))
        autor.save()
        categorias_data = validated_data.pop('categorias')
        artigo = Artigo.objects.create(**validated_data)
        categorias = []
        for categoria in categorias_data:
            categorias.append(Categoria.objects.get(**categoria))
        artigo.autor = autor
        artigo.categorias.set(categorias)
        artigo.save()
        return artigo

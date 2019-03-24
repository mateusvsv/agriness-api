# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Artigo, Autor


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = '__all__'


class ArtigoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artigo
        fields = '__all__'

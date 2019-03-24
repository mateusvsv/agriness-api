# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from categoria.models import Categoria


class Autor(models.model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Artigo(models.model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultima_modificacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
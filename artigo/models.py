# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from categoria.models import Categoria


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, related_name="categorias")
    data_criacao = models.DateTimeField(auto_now_add=True, blank=True)
    ultima_modificacao = models.DateTimeField(auto_now=True, blank=True)
    publicado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'

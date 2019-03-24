# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

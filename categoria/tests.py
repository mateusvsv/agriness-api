from rest_framework import status
from rest_framework.test import APITestCase
from .models import Categoria


class CategoriaTests(APITestCase):

    def test_criar_categoria(self):
        data = {'nome': 'Tec', 'descricao': 'Tec desc'}
        response = self.client.post('/categorias/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categoria.objects.count(), 1)
        self.assertEqual(Categoria.objects.get().nome, 'Tec')

    def test_listar_categorias(self):
        Categoria.objects.create(nome="Teste1")
        Categoria.objects.create(nome="Teste2")
        response = self.client.get('/categorias/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Categoria.objects.count())

    def test_atualizar_categoria(self):
        categoria = Categoria.objects.create(nome="Teste1", descricao='descricao')
        data = {'id': categoria.id, 'nome': 'teste2'}
        response = self.client.put('/categoria/' + str(categoria.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Categoria.objects.get().nome, 'teste2')

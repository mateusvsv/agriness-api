from rest_framework import status
from rest_framework.test import APITestCase
from .models import Artigo, Autor
from categoria.models import Categoria


class ArtigoTests(APITestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Teste1")
        self.autor = Autor.objects.create(nome='mateus', email='email@email.com')

    def test_criar_artigo(self):
        data = {'titulo': 'teste', 'conteudo': 'teste',
                'categorias': [{'id': self.categoria.id, 'nome': self.categoria.nome}],
                'autor': {'nome': 'mateus', 'email': 'mateus@gmail.com'}}
        response = self.client.post('/artigo/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artigo.objects.count(), 1)
        self.assertEqual(Artigo.objects.get().titulo, 'teste')

    def test_listar_artigos(self):
        Artigo.objects.create(titulo='teste1', conteudo='conteudo', autor=self.autor)
        Artigo.objects.create(titulo='teste2', conteudo='conteudo', autor=self.autor)
        response = self.client.get('/artigos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], Artigo.objects.count())

    def test_atualizar_artigo(self):
        artigo = Artigo.objects.create(titulo='teste2', conteudo='conteudo', autor=self.autor, publicado=True)
        data = {'id': artigo.id, 'titulo': 'teste2', 'conteudo': 'conteudo', 'publicado': False,
                'autor': {'id': artigo.autor.id, 'nome': self.autor.nome, 'email': self.autor.email},
                'categorias': [{'id': self.categoria.id, 'nome': self.categoria.nome}]}
        response = self.client.put('/artigo/' + str(artigo.id) + '/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Artigo.objects.get().publicado, False)

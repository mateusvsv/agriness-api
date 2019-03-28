from django.urls import path
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from artigo import views as ArtigoViews
from categoria import views as CategoriaViews


schema_view = get_swagger_view(title='Agriness CMS API - Endpoints')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artigos/', ArtigoViews.ArtigosListView.as_view()),
    path('artigo/', ArtigoViews.ArtigosCreateView.as_view()),
    path('artigo/<int:pk>/', ArtigoViews.ArtigoView.as_view()),
    path('categorias/', CategoriaViews.CategoriaListView.as_view()),
    path('categoria/', CategoriaViews.CategoriaView.as_view()),
    path('docs/', schema_view),
]

from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from artigo import views as ArtigoViews
from categoria import views as CategoriaViews


schema_view = get_swagger_view(title='Agriness CMS API - Endpoints')

urlpatterns = [
    path('artigos/', ArtigoViews.ArtigosListView.as_view()),
    path('artigo/<int:id>/', ArtigoViews.ArtigoView.as_view()),
    path('docs/', schema_view),
]

from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

from .views import *

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('books/export/csv', ExportBooksToCSV.as_view(), name='books-export-csv'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author-detail'),
    path('genres/', GenreList.as_view(), name='genre-list'),
    path('genres/<int:pk>', GenreDetail.as_view(), name='genre-detail'),
    path('publishers/', PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>', PublisherDetail.as_view(), name='publisher-detail'),
    path('languages/', LanguageList.as_view(), name='language-list'),
    path('languages/<int:pk>', LanguageDetail.as_view(), name='language-detail'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]

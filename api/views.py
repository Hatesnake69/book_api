import csv

from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.views import APIView

from api.models import Book, Author, Publisher, Genre, Language
from api.serializers import (
    BookSerializer, AuthorSerializer, PublisherSerializer, GenreSerializer, LanguageSerializer
)
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(tags=["Books"])
class ExportBooksToCSV(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.select_related('author', 'genre', 'publisher', 'language').all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="books.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Name', 'Author', 'Genre', 'Publisher', 'Language', 'Publication Date'])
        for book in books:
            writer.writerow([
                book.id,
                book.name,
                book.author.name if book.author else 'N/A',
                book.genre.name if book.genre else 'N/A',
                book.publisher.name if book.publisher else 'N/A',
                book.language.language if book.language else 'N/A',
                book.publication_date,
            ])
        return response


@extend_schema(tags=["Books"])
class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['author', 'genre', 'language', 'publisher']
    search_fields = ['name', 'author__name', 'genre__name', 'publisher__name']
    ordering_fields = ['name', 'publication_date']
    ordering = ['name']


@extend_schema(tags=["Books"])
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


@extend_schema(tags=["Authors"])
class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']


@extend_schema(tags=["Authors"])
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


@extend_schema(tags=["Genres"])
class GenreList(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']


@extend_schema(tags=["Genres"])
class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


@extend_schema(tags=["Publishers"])
class PublisherList(generics.ListCreateAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']


@extend_schema(tags=["Publishers"])
class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


@extend_schema(tags=["Languages"])
class LanguageList(generics.ListCreateAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['language']
    ordering_fields = ['language']
    ordering = ['language']


@extend_schema(tags=["Languages"])
class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()

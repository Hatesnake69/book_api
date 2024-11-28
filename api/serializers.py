from rest_framework import serializers

from api.models import Book, Author, Language, Publisher, Genre


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('__all__')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('__all__')

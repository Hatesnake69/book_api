from django.core.exceptions import ValidationError
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    language = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.language}"


class Book(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    publication_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="books")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'publication_date', 'author', 'genre', 'publisher', 'language'],
                name='unique_book_constraint'
            )
        ]

    def __str__(self):
        return f"{self.name} by {self.author}"

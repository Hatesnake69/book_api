from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from api.models import Book, Author, Genre, Publisher, Language


class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="John Doe")
        self.genre = Genre.objects.create(name="Fiction")
        self.publisher = Publisher.objects.create(name="Penguin")
        self.language = Language.objects.create(language="English")
        self.book_data = {
            "name": "New Book",
            "publication_date": "2024-01-01",
            "author": self.author.id,
            "genre": self.genre.id,
            "publisher": self.publisher.id,
            "language": self.language.id,
        }
        self.book = Book.objects.create(
            name="Old Book",
            publication_date="2023-01-01",
            author=self.author,
            genre=self.genre,
            publisher=self.publisher,
            language=self.language,
        )

    def test_01_create_book(self):
        response = self.client.post('/api/books/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Book")

    def test_02_list_books(self):
        Book.objects.create(
            name="Another Book",
            publication_date="2022-01-01",
            author=self.author,
            genre=self.genre,
            publisher=self.publisher,
            language=self.language,
        )
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[1]['name'], "Old Book")
        self.assertEqual(response.data[0]['name'], "Another Book")

    def test_03_update_book(self):
        updated_data = {
            "name": "Updated Book",
            "publication_date": "2024-06-01",
            "author": self.author.id,
            "genre": self.genre.id,
            "publisher": self.publisher.id,
            "language": self.language.id,
        }
        response = self.client.put(f'/api/books/{self.book.id}', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Book")
        self.assertEqual(response.data['publication_date'], "2024-06-01")

    def test_04_partial_update_book(self):
        partial_data = {"name": "Partially Updated Book"}
        response = self.client.patch(f'/api/books/{self.book.id}', partial_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Partially Updated Book")
        self.assertEqual(response.data['publication_date'], "2023-01-01")

    def test_05_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/api/books/{self.book.id}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_06_export_csv(self):
        response = self.client.get('/api/books/export/csv')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertIn('books.csv', response['Content-Disposition'])
        csv_content = response.content.decode('utf-8')
        self.assertTrue('ID,Name,Author,Genre,Publisher,Language,Publication Date' in csv_content)
        self.assertTrue('Old Book' in csv_content)
        self.assertTrue('John Doe' in csv_content)
        self.assertTrue('Fiction' in csv_content)
        self.assertTrue('Penguin' in csv_content)
        self.assertTrue('English' in csv_content)
        self.assertTrue('2023-01-01' in csv_content)



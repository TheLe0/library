from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=35)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=45)
    edition = models.CharField(max_length=15)
    publication_year = models.IntegerField()

    class Meta:
        ordering = ['publication_year', 'title']

    def __str__(self):
        return self.title


class BookAuthor(models.Model):

    book = models.ForeignKey('api.Book', on_delete=models.CASCADE)
    author = models.ForeignKey('api.Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title+" - "+self.author.name

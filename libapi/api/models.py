from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=35) 

    def __str__(self):
        return self.name  

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.ForeignKey('api.Book', on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return self.title

class Edition(models.Model):
    number = models.CharField(max_length=5)
    year = models.IntegerField()
    book = models.ForeignKey('api.Book', on_delete=models.CASCADE, related_name='editions')

    def __str__(self):
        return self.title


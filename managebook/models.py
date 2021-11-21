from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.TextField()
    isbn = models.TextField()
    authors = models.ManyToManyField(Author)
    number_of_pages = models.IntegerField()
    publisher = models.TextField()
    country = models.TextField()
    release_date = models.DateField()

    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name
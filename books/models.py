from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()

    def __str__(self):
        return self.title

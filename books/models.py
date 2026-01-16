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
    # student_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Bookrent(models.Model):
    user = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    rented_at = models.DateTimeField(auto_now_add=True)  
    returned = models.BooleanField(default=False)
    # student_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
    
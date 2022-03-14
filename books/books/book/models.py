from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pages = models.CharField(max_length=5)
    year_published = models.CharField(max_length=4)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Book_pic(models.Model):
    img = models.ImageField(upload_to='book_img')
    name_of_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name_of_book.title
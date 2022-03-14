from django.contrib import admin
from .models import Book, Book_pic

# Register your models here.
@admin.register(Book)
class Book_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'year_published', 'date_created')

admin.site.register(Book_pic)
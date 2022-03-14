from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    book_img = forms.ImageField()

    class Meta:
        model = Book
        exclude = ('user',)
from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BookForm
from .models import Book, Book_pic

# Create your views here.ls
def index(request):

    book_list = Book.objects.all()
    context = {'book_list':book_list}
    return render(request, 'book/index.html', context)

def book_details(request, book_id):

    details = Book.objects.get(id=book_id)
    picture = Book_pic.objects.filter(name_of_book=details).first() #name_of_pic is from the model
    context = {
        'details':details, 'picture':picture
        }
    return render(request, 'book/book_details.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
    
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user()
            book.save()

            book_img = form.cleaned_data['book_img']
            Book_pic.objects.create(img=book_img, book=book)

            redirect(reverse('fav_books:book_index'))
        else:
            return render(request, 'book/add_book.html', {'form':form})
    else:
        form = BookForm()

    return render(request, 'book/add_book.html', {'form':form})

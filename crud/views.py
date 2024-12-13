from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# Create View
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

# Read View
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Update View
def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('crud:book_list')  # Kitob yangilanganidan so'ng kitoblar ro'yxatiga qaytish
    else:
        form = BookForm(instance=book)

    return render(request, 'update_book.html', {'form': form, 'book': book})

# Delete View
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()  # Kitobni o'chirish
        return redirect('crud:book_list')  # O'chirilgandan so'ng kitoblar ro'yxatiga qaytish

    return render(request, 'delete_book.html', {'book': book})

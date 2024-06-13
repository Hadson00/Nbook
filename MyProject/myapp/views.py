from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'site/index.html',{"books": Book.objects.all()})

@login_required
def home(request):
    book = Book.objects.all()
    return render(request, 'site/home.html', {'books': book})

@login_required
def like_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    like, created = Like.objects.get_or_create(user=request.user, book=book)
    if not created:
        like.delete()
    return redirect('card_detail', book_id=book_id)

@login_required
def comment_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, book=book, content=content)
    return redirect('card_detail', book_id=book_id)

@login_required
def card_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = Comment.objects.filter(book=book)
    liked = False
    if request.user.is_authenticated:
        liked = Like.objects.filter(user=request.user, book=book).exists()
    return render(request, 'site/card_detail.html', {'books': book, 'comments': comments, 'liked': liked})

@login_required
def create(request):
    form = BookForm
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "site/create.html", {"forms":form})

@login_required
def edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro editado com sucesso!')
            return redirect('index')
    else:
        form = BookForm(instance=book)
    return render(request, "site/update.html",{"form":form, "books":book})

@login_required
def update(request, id):
    try:
        if request.method == "POST":
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                messages.success(request, 'Livro foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')

@login_required            
def read(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "site/read.html", {"books":book})

@login_required
def delete(request, id):
    item = Book.objects.get(pk=id)
    item.delete()
    messages.success(request, 'Livro foi deletada com sucesso!')
    return redirect('index')
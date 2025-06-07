from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Book, Author
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_user = authenticate(username=username, password=password)
        if  auth_user:
            login(request, auth_user)
            return redirect(request.GET.get('next') or 'author_page')
        else: 
            messages.error(request, 'username or password is incorrect!')
            return redirect('login_page')
    
    if 'next' in request.GET:
        messages.error(request, 'please login to access this page')
    return render(request, 'login.html')


def create_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists!')
            return redirect('create_page')
        
        if password:
            query_set = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                username=username,
                                                password=password, email=email)
            query_set.save()
            messages.success(request, 'user created successfully')
            return redirect('create_page')
        else:
            messages.error(request, 'password is required')
            return redirect('create_page')
    return render(request, 'create.html')


def post_page(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        content = request.FILES.get('content')
        author_id = request.POST.get('author_id')
        title = request.POST.get('title')

        author = Author.objects.get(id=author_id)
        book = Book.objects.create(content=content, title=title, author=author,)
        book.save()
        return redirect('book_list')
    
    return render(request, 'blog.html', {'authors': authors})


@login_required(login_url='login_page')
def book_list(request):
    return render(request, 'book_list.html', {'books':Book.objects.select_related('author').all()})


def author_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if Author.objects.filter(name=name).exists():
            messages.error(request, 'author already exists!')
            return redirect('author_page')
        else:
            query_set = Author.objects.create(name=name)
            query_set.save() 
            return redirect('post_page')
    return render(request, 'author.html')


def log_out(request):
    logout(request)
    return redirect('login_page')


def remove_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'DELETE': 
        book.delete()
        return JsonResponse({'success':'book deleted successfully'}, status=200)
    return JsonResponse({'error':'method not allowed'}, status=405)


def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    author = Author.objects.all()
            
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        author = get_object_or_404(Author, id=author_id)
        book.author = author
        book.content = request.FILES.get('content')
        book.title = request.POST.get('title')
        
        book.save()
        return redirect('book_list')
    return render(request, 'update.html', {'author':author, 'book':book})


def author_list(request):
    authors = Author.objects.annotate(book_count=Count('book'))
    return render(request, 'author_list.html', {'authors':authors, 'books':Book.objects.all()})

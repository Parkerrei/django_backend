from django.urls import path
from .views import update_book, remove_book, login_page, create_page, post_page , log_out, author_page, book_list , author_list  # If 'account' is a module with a view named 'account'

urlpatterns = [
    path('', login_page, name='login_page'),
    path('create_page/', create_page, name='create_page'),
    path('post_page/', post_page, name='post_page'),
    path('author_page/', author_page, name='author_page'),
    path('log_out/', log_out, name='log_out'),
    path('book_list/', book_list, name='book_list'),
    path('remove_book/<int:book_id>/', remove_book, name='remove_book'),
    path('update_book/<int:id>/', update_book, name='update_book'),
    path('author_list/', author_list, name='author_list'),

]

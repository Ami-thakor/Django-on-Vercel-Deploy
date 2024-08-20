
from django.urls import path
from .views import*
urlpatterns = [
    path('',home,name='home'),
    path('blog/',blog,name='blog'),
    path('cart/',cart,name='cart'),
    path('category/',category,name='category'),
    path('checkout/',checkout,name='checkout'),
    path('confirmation/',confirmation,name='confirmation'),
    path('contact/',contact,name='contact'),
    path('elements/',elements,name='elements'),
    path('login/',login,name='login'),
    path('single_blog/',single_blog,name='single_blog'),
    path('single_product/',single_product,name='single_product'),
    path('tracking/',tracking,name='tracking'),
    # path('home/',home,name='home'),


]

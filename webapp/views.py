from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'files/index.html')

def cart(request):
    return render(request,'files/cart.html')



def blog(request):
    return render(request,'files/blog.html')


def category(request):
    return render(request,'files/category.html')


def checkout(request):
    return render(request,'files/checkout.html')


def confirmation(request):
    return render(request,'files/confirmation.html')


def elements(request):
    return render(request,'files/elements.html')


def login(request):
    return render(request,'files/login.html')


def single_product(request):
    return render(request,'files/single-product.html')



def tracking(request):
    return render(request,'files/tracking.html')



def single_blog(request):
    return render(request,'files/single-blog.html')

def contact(request):
    return render(request,'files/contact.html')



# def home(request):
#     return render(request,'files/home.html')

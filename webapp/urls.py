from django.urls import path
from . import views



#>>>>>  this is "Shop" Urls


urlpatterns = [
    path('',views.home,name="home"),
    
    
   
]
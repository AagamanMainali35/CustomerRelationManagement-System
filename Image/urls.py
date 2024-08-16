from django.contrib import admin
from django.urls import path
from Core.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',home,name='Homepage'),
    path('Procuct-form/',product_form,name='productForm'),
    path('Customer-Form/',customer_form,name='customerForm'),
    path('details/',customer_details,name='customerdetails'),
    path('update/<int:id>',update, name='update'),
    path('delete/<int:id>',delete,name='deleteuser'),
    path('register/',register,name='register'),
    path('login/',loginuser,name='loginuser'),
    path('logout',logouts,name='logout'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
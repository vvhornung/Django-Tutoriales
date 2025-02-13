from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ContactPageView
from django.views.generic import TemplateView

urlpatterns = [
 path('', HomePageView.as_view(), name='home'),
 path('about/', AboutPageView.as_view(), name='about'),
 path('contact/', ContactPageView.as_view(), name='contact'),
 path('products/create/', ProductCreateView.as_view(), name='form'),
 path('products/created/', TemplateView.as_view(template_name='products/created.html'), name='product-created'),
 path('products/', ProductIndexView.as_view(), name='products'),
 path('products/<str:id>', ProductShowView.as_view(), name='show'),
 
]
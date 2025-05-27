from django.urls import path
from .import views
from .views import fomu_view

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('fomu/', fomu_view, name='fomu'),

]
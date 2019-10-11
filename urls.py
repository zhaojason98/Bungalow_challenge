from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:zillow_id>', views.details, name='details')
    path('<int:zillow_id>/description', views.description, name='description'),
    path('<int:zillow_id>/price', views.price, name='price'),
    path('<int:zillow_id>/estimate', views.estimate, name='estimates'),
    path('<int:zillow_id>/tax', views.tax, name='tax'),
    path('<int:zillow_id/location', views.location, name='location')
]
from django.urls import path
from .views import HomePageView, AboutPageView, HelpPageView, NewsPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('help/', HelpPageView.as_view(), name='help'),
    path('news/', NewsPageView.as_view(), name='news'),
    
]

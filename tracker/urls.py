from django.urls import path

from .views import AboutSpacexView, HomeView


urlpatterns = [
   path('', HomeView.as_view(), name="home"),
   path('aboutspacex/', AboutSpacexView.as_view(), name="aboutspacex")
]
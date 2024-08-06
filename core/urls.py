from django.urls import path
from .views import HomePageView, STHIPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sthi/', STHIPageView.as_view(), name="sthi" ),
]

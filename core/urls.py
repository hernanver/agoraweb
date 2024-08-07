from django.urls import path
from .views import HomePageView, STHIPageView, SuaraPageView, AgroecobotPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sthi/', STHIPageView.as_view(), name="sthi" ),
    path('suara/', SuaraPageView.as_view(), name="suara" ),
    path('agroecobot/', AgroecobotPageView.as_view(), name="agroecobot" ),


]

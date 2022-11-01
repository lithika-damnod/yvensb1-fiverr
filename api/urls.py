from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.user_actions, name="user_actions"),
    path("user/<int:user_id>/", views.specific_user_actions,
         name="specific_user_actions"),
    path("ad/", views.ad_actions, name="ad_actions"),
    path("ad/<int:ad_id>", views.specific_ad_actions,
         name="specific_ad_actions"),
    path("car/", views.car_actions, name="car_actions"),
    path("car/<int:car_id>", views.specific_car_actions,
         name="car_actions"),
]

from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.index, name='horoscope_index'),
#     path('type/', views.type),
#     path('type/<element>/', views.type2),
#     path('<int:sign_zodiak>/', views.get_info_about_sign_by_number),
#     path('<str:sign_zodiak>/', views.get_info_about_sign, name='horoscope-name'),
#
# ]
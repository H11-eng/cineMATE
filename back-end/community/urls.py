from django.urls import path
from . import views


app_name = "community"
urlpatterns = [
#   path('sign-up/', views.signup, name="sign_up"),
    path('reviews/', views.review_list, name='review_list'),  
    path('reviews/<int:review_pk>/', views.review_detail, name='review_detail'),  
    path('reviews/<int:review_pk>/comments/', views.comment_list, name='comment_list'),  
    path('reviews/<int:review_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),  
    path('movieforyou/', views.movieforyou_list, name='movieforyou_list'),  
    path('movieforyou/<int:movie_pk>/', views.movieforyou_detail, name='movieforyou_detail'),  
]

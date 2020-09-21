from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('rooms/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('games/<slug:slug>/', views.GameDetail.as_view(), name='game_detail'),
    path('rooms', views.PostPage.as_view(), name='rooms'),
    path('games', views.GamePage.as_view(), name='games'),
    path('contact', views.contact, name="contact"),
    path('faq', views.FaqList.as_view(), name = 'faq'),
    path('deals', views.deals, name = 'deals'),
    path('book-now', views.error, name = 'book-now'),
    path('about-us', views.about, name = 'about-us'),
    path('404', views.error, name = '404'),
] 

from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('games', views.PostPage.as_view(), name='games'),
    path('contact', views.contact, name="contact"),
    path('faq', views.FaqList.as_view(), name = 'faq'),
    path('deals', views.deals, name = 'deals'),
    path('book-now', views.book, name = 'book-now'),
] 

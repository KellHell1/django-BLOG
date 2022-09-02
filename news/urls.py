from django.urls import path
from . import views

urlpatterns = [
    path('',views.news_home, name='news_home'),
    path('news/create/', views.create, name='create'),
    path('<int:pk>', views.NewsTemplateView.as_view(), name="news-detail"),
    path("<int:pk>/update", views.NewsUpdateView.as_view(), name="news-update"),
    path("<int:pk>/delete", views.NewsDeleteView.as_view(), name="news-delete")

]

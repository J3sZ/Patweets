from django.urls import path
from .views import PostAPIView, PostAPIDetail

urlpatterns = [
    path('', PostAPIView.as_view(), name ='Post_list'),
    path('<int:pk>/', PostAPIDetail.as_view(), name = 'Post_Detail'),
]
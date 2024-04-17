from rest_framework import generics

# Create your views here.
from patweets.models import Post
from .serializers import PostSerializer

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
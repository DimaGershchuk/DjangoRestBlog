from django_filters import rest_framework as filters
from .models import Post, Comment


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title']


class CommentFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__username', lookup_expr='icontains')

    class Meta:
        model = Comment
        fields = ['author']

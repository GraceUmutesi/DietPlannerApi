from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_deleted=False)
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filterset_fields = ['id', 'title', 'created_at', 'created_by']
    search_fields = ['id', 'title']
    ordering_fields = ['title', 'created_at']

    def destroy(self, request, *args, **kwargs):
        response = {'detail': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

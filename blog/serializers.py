from rest_framework import serializers

from blog.models import Article
from users.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ('is_deleted', )

    def to_representation(self, instance):
        serialized_data = super(ArticleSerializer, self).to_representation(instance)

        serialized_data['created_by'] = UserSerializer(instance.created_by).data

        return serialized_data

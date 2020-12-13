from rest_framework import serializers

from . models import Feedback
from . models import Post
from . models import User2


class User2Serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return User2.objects.create(**validated_data)


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=1000)
    author_id = serializers.IntegerField()
    created_at = serializers.DateField()
    date_delete = serializers.DateField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class FeedbackSerializer(serializers.Serializer):
    theme = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=1000)
    created_at = serializers.DateField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)

    def update(self, feedback, validated_data):
        feedback.title = validated_data.get('title', feedback.theme)
        feedback.description = validated_data.get('description', feedback.description)
        feedback.email = validated_data.get('body', feedback.email)
        feedback.save()

        return feedback



# можно указать exclude вместо fields
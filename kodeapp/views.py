from django.shortcuts import render
from rest_framework import request
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Feedback
from .models import Post
from .models import User2
from .serializers import FeedbackSerializer, PostSerializer, User2Serializer


class User2View(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user2 = User2.objects.all()
        serializer = User2Serializer(user2, many=True)

        return Response({'users2': serializer.data})


class PostView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)

        return Response({'post': serializer.data})


class FeedbackView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)

        return Response({'feedback': serializer.data})


    def post(self, request):
        feedback = request.data.get('feedback')
        serializer = FeedbackSerializer(data=feedback)
        if serializer.is_valid(raise_exception=True):
            feedback_saved = serializer.save()

            return Response({'success': f"feedback '{feedback_saved.theme}' created successfully"})


class FeedbackByIDView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        feedback = get_object_or_404(Feedback.objects.all(), pk=pk)
        data = request.data.get('feedback')
        serializer = FeedbackSerializer(instance=feedback, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            feedback_saved = serializer.save()

            return Response({'success': f"feedback '{feedback_saved.theme}' updated successfully"})

    def delete(self, request, pk):
        feedback = get_object_or_404(Feedback.objects.all(), pk=pk)
        feedback.delete()

        return Response({'success': f"feedback '{pk}' deleted successfully"}, status=204)
from django.urls import path

from .views import FeedbackView, FeedbackByIDView, PostView, User2View

app_name = 'kodeapp'

urlpatterns = [
    path('feedback/', FeedbackView.as_view()),
    path('feedback/<int:pk>', FeedbackByIDView.as_view()),
    path('post/', PostView.as_view()),
    path('user2/', User2View.as_view()),
]


from django.db import models


class User2(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User2, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    date_delete = models.DateField(auto_now_add=True)
    test_data = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    theme = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return self.theme






from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_image/%Y/%m/%d/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class ObjectCount(models.Model):
    name = models.CharField(max_length=50, unique=True)  # 객체 이름 (예: person)
    count = models.PositiveIntegerField(default=0)        # 누적 감지 횟수

    def __str__(self):
        return f"{self.name}: {self.count}"

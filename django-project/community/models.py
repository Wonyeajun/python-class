from django.db import models
from django.conf import settings

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('love', '연애'),
        ('friend', '친구'),
        ('family', '가족'),
        ('study', '학업/진로'),
        ('etc', '기타'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='etc')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts", blank=True)
    thumbs = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="thumb_posts", blank=True)
    sads = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="sad_posts", blank=True)

    def __str__(self):
        return self.title

    @property
    def total_reactions(self):
        return self.likes.count() + self.thumbs.count() + self.sads.count()


# 에러 원인이었던 Comment 모델
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.content[:10]}"
from django.db import models
from django.conf import settings

class Tree(models.Model):
    page_number = models.IntegerField(default=1, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page_number}번째 나무"

    @property
    def is_full(self):
        return self.fruits.count() >= 20


class Fruit(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE, related_name='fruits')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.tree.page_number}번 나무] {self.content[:10]}"
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField()
    #在Django管理界面可以正常显示标题
    def __str__(self):
        return self.title

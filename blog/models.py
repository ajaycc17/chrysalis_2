from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Topic(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100, default='Ajay Choudhury')
    thumbnail = models.ImageField(upload_to='blog')
    category = models.ForeignKey(
        Topic, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, default="")
    timeStamp = models.DateTimeField(blank=True)
    publish = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:20] + "..." + "by" + self.user.first_name

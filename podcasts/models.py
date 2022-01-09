from django.db import models


class Episodes(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=320)
    content = models.TextField()
    author = models.CharField(max_length=200, default='Chrysalis Team')
    anchor_link = models.CharField(max_length=512)
    slug = models.SlugField(max_length=150, default="")
    timeStamp = models.DateTimeField(blank=True)
    publish = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

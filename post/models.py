from django.db import models

import datetime


# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=255)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def getTimeAgo(self):

        now = datetime.datetime.now(tz=self.created_at.tzinfo)

        diff = now - self.created_at

        if diff.days > 0:

            return f"{diff.days} days ago"

        elif diff.seconds > 3600:

            return f"{diff.seconds // 3600} hours ago"

        elif diff.seconds > 60:

            return f"{diff.seconds // 60} minutes ago"

        else:

            return f"{diff.seconds} seconds ago"

    def get_absolute_url(self):

        return f"/post/{self.id}"


class Tags(models.Model):

    name = models.CharField(max_length=255)

    posts = models.ManyToManyField(Post, related_name="tags")

    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

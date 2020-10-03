from django.db import models
from ..tasks import twitter_post
from django.utils import timezone


class TwitterPost(models.Model):
    uuid = models.UUIDField(unique=True, null=False)
    content = models.TextField(max_length=280, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True, blank=True)

    __original_content = None
    __original_publish_date = None

    def __init__(self, *args, **kwargs):
        super(TwitterPost, self).__init__(*args, **kwargs)
        self.__original_content = self.content
        self.__original_publish_date = self.publish_date

    def save(self, *args, **kwargs):

        if not self.id:
            if timezone.now() <= self.publish_date:
                twitter_post.apply_async(kwargs={"status": self.content}, eta=self.publish_date)
            else:
                twitter_post.delay(self.content)
        elif (self.content != self.__original_content) or (self.publish_date != self.__original_publish_date):
            if timezone.now() <= self.publish_date:
                twitter_post.apply_async(kwargs={"status": self.content}, eta=self.publish_date)
            else:
                twitter_post.delay(self.content)

        super().save(*args, **kwargs)
from django.db import models
from django_comments import models as django_comments_models
# from django.db.models.base import Model

# we did not add
class MyComment(django_comments_models.Comment):
    #comment = models.ForeignKey(comments.models.Comment)
    # theme = models.CharField(max_length=150, default='')
    # phone = models.CharField(max_length=150, default='')
    image	= models.ImageField(max_length=255, upload_to='comments')

"""
class MonkeyPatch(object):
    def process_request(self, request):
        from django.contrib.comments.models import Comment as cc
        cc._meta.fields.append(image)
        # cc._meta.fields.append(theme)
        # cc._meta.fields.append(phone)
"""
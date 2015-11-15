from django.contrib.comments import Comment
from django.contrib.comments.moderation import CommentModerator, moderator
from cms.models import Page
from django.contrib import admin
from customcomments import MyComment


class PageModerator(CommentModerator):
    email_notification = True

    def moderate(self, comment, content_object, request):
        return True

moderator.register(Page, PageModerator)

admin.site.register(MyComment)


from django.contrib import admin
from django.utils.translation import ugettext_lazy as _, ungettext

from django_comments.admin import CommentsAdmin
from customcomments import MyComment


class MyCommentsAdmin(CommentsAdmin):
  fieldsets = (
      (
          None,
          {'fields': ('content_type', 'object_pk', 'site')}
      ),
      (
          _('Content'),
          {'fields': ('user', 'user_name', 'image', 'user_email', 'user_url', 'comment')}
      ),
      (
          _('Metadata'),
          {'fields': ('submit_date', 'ip_address', 'is_public', 'is_removed')}
      ),
  )

  list_display = ('name', 'image', 'content_type', 'object_pk', 'ip_address', 'submit_date', 'is_public', 'is_removed')

admin.site.register(MyComment, MyCommentsAdmin)

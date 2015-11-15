from models import MyComment
from django.contrib.comments.models import Comment
from django.db import models

from .forms import MyCommentForm

def get_model():
    return MyComment

def get_form():
    return MyCommentForm

MyComment.add_to_class('image', models.ImageField(max_length=255, upload_to='comments'))


from django import forms
from django.contrib.comments.models import Comment
from django.contrib.comments.forms import CommentForm, COMMENT_MAX_LENGTH, CommentSecurityForm
from django.forms.forms import DeclarativeFieldsMetaclass
from django.utils.translation import ungettext, ugettext_lazy as _
#from captcha.fields import CaptchaField
from customcomments import MyComment


class CommentMetaclass(DeclarativeFieldsMetaclass):
    def __init__(cls, cls_name, cls_bases, dict):
        super(CommentMetaclass, cls).__init__(cls_name, cls_bases, dict)

class MyCommentForm(CommentForm):

    __metaclass__ = CommentMetaclass

    def __init__(self, target_object, data=None, initial=None, files=None):
        self.target_object = target_object
        if initial is None:
            initial = {}
        initial.update(self.generate_security_data())
        super(CommentSecurityForm, self).__init__(data=data, initial=initial, files=files)

    name          = forms.CharField(label=_("Name"), max_length=50, widget=forms.TextInput(attrs={'class' : 'validate[required] required', 'placeholder' : _("Name") }), )
    url           = forms.CharField(label=_("Phone"), max_length=50, widget=forms.TextInput(attrs={'class' : '', 'placeholder' : _("Phone") }), required=False)
    email         = forms.EmailField(label=_("Email"), widget=forms.TextInput(attrs={'class' : 'validate[required,email] required', 'placeholder' : _("Email") }), )
    comment       = forms.CharField(label=_('Text'), widget=forms.Textarea(attrs={'class' : 'validate[required] required', 'placeholder' : _("Text") }),  max_length=COMMENT_MAX_LENGTH)
    image         = forms.ImageField(label=_('Image'), required=False)
    #captcha       = CaptchaField()

    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return MyComment

    def get_comment_create_data(self):
        # Use the data of the superclass, and add in the title field
        data = super(CommentForm, self).get_comment_create_data()
        data['image'] = self.cleaned_data['image']
        return data

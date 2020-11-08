from django.forms import ModelForm, Textarea

from BairBudalite.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': Textarea(attrs={'placeholder': 'Оставете коментар',
                                       'id': 'message'})
        }

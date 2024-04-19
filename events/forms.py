from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

    class Meta:
        model = Comment
        fields = ('body',)
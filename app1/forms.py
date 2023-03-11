from django import forms

from app1.models import Text


class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Text
        fields = ['text']

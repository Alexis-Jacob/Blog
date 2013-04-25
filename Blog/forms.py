from django import forms

class   CommentForm(forms.Form):
    author = forms.CharField(max_length=20)
    content = forms.CharField(widget = forms.Textarea)

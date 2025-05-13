from unittest.util import _MAX_LENGTH
from django import forms

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your Mail",max_length=200)
    name=forms.CharField(label="Enter your name",max_length=100)
    feedback=forms.CharField(label="your feedback",widget=forms.Textarea)

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

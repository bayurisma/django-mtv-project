from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=20)
    description = forms.CharField(
        widget = forms.Textarea
    )
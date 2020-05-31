from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
        widget=forms.TextInput(
            attrs={'class' : 'form-control','placeholder' : 'Enter todo e.g. Feed the cat', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))
    important = forms.BooleanField(required=False)

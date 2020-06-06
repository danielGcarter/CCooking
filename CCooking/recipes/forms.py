from django import forms

class recipeForm(forms.Form):
    title = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Recipe Name"
        }))
    author = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        }))
    background = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Recipe Background"
        }))
    category = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Category"
        }))
    process = forms.CharField(widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Please input steps here..."
    }))
    
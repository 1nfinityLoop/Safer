from django import forms




class search(forms.Form):
    ville = forms.CharField(max_length=10)
    categorie = forms.IntegerField()


from django import forms
from coreapi.models import FileTable

class SearchForms(forms.ModelForm):
    search = forms.CharField(widget=forms.TextInput(attrs={'id': "search"}))

    class Meta:
        model = FileTable
        fields = ('search',)
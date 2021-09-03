from django import forms
from django.forms import ModelForm
from .models import Table


# class TableForm(forms.ModelForm):
#     class Meta:
#         model = Table
#         fields = ('city',)

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


class ModelDataForm(ModelForm):
    class Meta:
        model = Table
        exclude = ('city','word_TF','word_IDF')

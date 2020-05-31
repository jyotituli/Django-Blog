from django.forms import ModelForm
from .models import blog


class UploadForm(ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'text', 'image']

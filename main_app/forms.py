from django.forms import ModelForm
from .models import Polished

class PolishedForm(ModelForm):
    class Meta:
        model = Polished
        fields = ['date', 'polish']
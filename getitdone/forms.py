from django.forms import ModelForm
from .models import Getitdone
# todo is the ModelForm refer viewtodo
class GetitdoneForm(ModelForm):
    class Meta:
        model=Getitdone
        fields=['title','memo','important',]
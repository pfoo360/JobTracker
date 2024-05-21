from django.forms import ModelForm
from .models import *

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'role', 'status', 'link']


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['job', 'comment']
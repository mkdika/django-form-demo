from django import forms
from .models import Author
from django.contrib.admin.widgets import AdminDateWidget
from ckeditor.widgets import CKEditorWidget


class AuthorForm(forms.ModelForm):

    bio = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Author
        fields = '__all__'
        
        widgets = {
            'birth_date': forms.DateInput(format="%d %d %Y", attrs={'type': 'date', }),
            'reminder_time': forms.TimeInput(format="%H:%M", attrs={'type': 'time', }),
            'member_type': forms.RadioSelect(),
        }

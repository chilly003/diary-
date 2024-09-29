from .models import APP
from django import forms

class APPFORM(forms.ModelForm):
    class Meta:
        model = APP
        fields = ('work','todo')
        widget = {
            'work' : forms.TextInput(
                attrs= {
                    'label':'할일'
                }
            ),
            'todo': forms.Textarea(
                attrs={
                    'label':'뭘해야하는지'
                }
            )
        }
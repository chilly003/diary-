from django import forms
from . models import APP

class APPFORM(forms.ModelForm):
    class Meta:
        model = APP
        fields = ('name','report','image')
        widget = {
            'name' : forms.TextInput(
                attrs= {
                    'label' : '이름',
                }
            ),
            'report' : forms.Textarea(
                attrs= {
                    'label' : '내용'
                }
            ),
        }
        label = {
            'image' : '사진'
        }
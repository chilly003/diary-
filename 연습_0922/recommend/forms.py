from django import forms
from . models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': '제목을 입력해주세요.',
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '저자를 입력해주세요.',
                }
            ),
            'report': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '독후감을 작성해 주세요.',
                }
            ),
        }
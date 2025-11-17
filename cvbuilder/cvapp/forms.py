from django import forms
from .models import CV, CVTemplate

class CVForm(forms.ModelForm):
    selected_template = forms.ModelChoiceField(
        queryset=CVTemplate.objects.filter(active=True),
        empty_label="Select CV Template"
    )

    class Meta:
        model = CV
        exclude = ['owner', 'created_at', 'updated_at']
        fields = ['title', 'selected_template', 'name', 'email', 'phone', 'location', 'summary', 'photo', 'skills', 'experience', 'education', 'projects']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4}),
            'skills': forms.Textarea(attrs={'rows': 2}),
        }

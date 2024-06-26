from django import forms

from .models import ConversationMassage

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMassage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }) 
        }
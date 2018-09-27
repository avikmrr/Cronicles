from django import forms

from .models import TextSpeech

class TextSpeechForm(forms.ModelForm):
	class Meta:
		model = TextSpeech
		fields = ['text','language','filename']
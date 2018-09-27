from django import forms


class UploadApkViaUrlForm(forms.Form):
    url = forms.CharField(max_length=500)
from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(label="Select a file")
    action = forms.ChoiceField(choices=[('line_count', 'Line Count'), ('word_count', 'Word Count')])

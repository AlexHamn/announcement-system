from django import forms

class AnnouncementForm(forms.Form):
    def __init__(self, *args, **kwargs):
        variables = kwargs.pop('variables', [])
        super().__init__(*args, **kwargs)

        for variable in variables:
            self.fields[variable] = forms.CharField(label=variable, required=True)
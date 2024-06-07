# homepage/forms.py

from django import forms
from django.core.validators import RegexValidator
from .models import Subcategory

class AnnouncementForm(forms.Form):
    def __init__(self, *args, **kwargs):
        variables = kwargs.pop('variables', [])
        super().__init__(*args, **kwargs)

        variable_patterns = {
            'flight_number': RegexValidator(r'^[A-Z]{2}\s\d+[A-Z]?$', 'Flight number must be in the format "XX 123A".'),
            'origin': RegexValidator(r'^[A-Z]{3}$', '(e.g. LAX, JFK, LHR).'),
            'destination': RegexValidator(r'^[A-Z]{3}$', '(e.g. LAX, JFK, LHR).'),
            'gate_number': RegexValidator(r'^\d+$', '(e.g. 12, 45, 103).'), 
            'reason': RegexValidator(r'^(?!\s*$)(?:[a-z]+(?:\s+[a-z]+){0,49})$', '(e.g. "delayed by weather", "mechanical issues", "waiting for connecting flight").'),
            'new_time': RegexValidator(r'^(0\d|1\d|2[0-3]):[0-5][0-9]$', '(e.g. 14:30, 09:45, 22:00).'),
            'time_remaining': RegexValidator(r'^(?:[0-5]?\d|60)$', '(e.g. 15, 30, 45, 60).'),
        }

        for variable in variables:
            validator = variable_patterns.get(variable)
            label = variable.replace('_', ' ').title()
            self.fields[variable] = forms.CharField(
                label=label,
                required=True,
                validators=[validator] if validator else []
            )

class SubcategoryForm(forms.ModelForm):
    predefined_parts = forms.CharField(widget=forms.Textarea, help_text="Enter each predefined part on a new line.")

    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'template', 'template_ru', 'template_kg', 'predefined_parts']
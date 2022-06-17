from django import forms
from .models import Contact

class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contactname','contactlastname','contactemail','contactdescription',]

    def __init__(self, *args, **kwargs):
        super(ContactFrom, self).__init__(*args, **kwargs)
        self.fields['contactname'].error_messages = {
            'required': 'Please enter name'
        }
        self.fields['contactlastname'].error_messages = {
            'required': 'Please enter lastname'
        }
        self.fields['contactemail'].error_messages = {
            'required': 'Please enter email@example.com'
        }
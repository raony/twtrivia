from django import forms
from artwark.models import Participante

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        exclude = ['imagens']

    def __init__(self, *args, **kwargs):
        super(ParticipanteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

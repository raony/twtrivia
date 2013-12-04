from django import forms
from trivia.models import Jogador

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        exclude = ['melhor_tempo']

    def __init__(self, *args, **kwargs):
        super(JogadorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

from django.forms.models import model_to_dict
from webdev.consultas.models import Consulta
from django.forms import ModelForm, fields


class ConsultaNewForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['ticket_id']

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['ticket_id','approved']
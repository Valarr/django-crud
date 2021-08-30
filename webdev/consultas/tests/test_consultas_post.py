import pytest
from django.urls import reverse
from webdev.consultas.models import Consulta


@pytest.fixture
def response(client, db):
    resp = client.get(reverse('consultas:home'), data={'input-ticket':'Consulta'})
    return resp

def test_consulta_exists_on_db(response):
    assert Consulta.objects.exists()


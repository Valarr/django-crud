import pytest
from django.urls import reverse
from webdev.consultas.models import Consulta


@pytest.fixture
def response(client, db):
    resp = client.post(reverse('consultas:home'), data={'ticket_id': 'Consulta'})
    return resp

def test_consulta_exists_on_db(response):
    assert Consulta.objects.exists()

def test_redirect_after_send(response):
    assert response.status_code == 302 #redirect

@pytest.fixture
def response_invalid(client, db):
    resp = client.post(reverse('consultas:home'), data={'ticket_id': ''})
    return resp

def test_consulta_invalid_data(response_invalid):
    assert not Consulta.objects.exists()

def test_invalid_data_page(response_invalid):
    assert response_invalid.status_code == 400 
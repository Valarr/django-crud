from django.urls import reverse

def test_status_code(client):
    response = client.get(reverse('consultas:home'))
    assert response.status_code == 200
from datetime import date, timedelta
from random import randint
import pytest


@pytest.mark.controllers
@pytest.mark.register_resource
class RegisterUserTests:
    def setup_class(self):
        self.url = '/api/v1/auth/users/register/'
        self.base_payload = {
            'username': 'user01',
            'email': 'example@email.com',
            'password': 'Strongpassword123@',
            'first_name': 'John',
            'last_name': 'Doe',
            'birthdate': '2000-01-01',
            'phone_number': '11996857412'
        }
    
    def generate_payload(self, username=None, email=None):
        payload = self.base_payload.copy()
        if username is not None:
            payload['username'] = username
        if email is not None:
            payload['email'] = email
        return payload

    def test_register_user_success(self, client):
        payload = self.generate_payload(username='user05', email='email-ex@email.com')

        response = client.post(self.url, json=payload)

        assert response.status_code == 201
        assert response.headers['Location'] is not None
        
        response_json = response.json

        assert response_json.get('success')
        assert response_json.get('id')
        assert response_json.get('message') == 'Usuário registrado com sucesso.'

    def test_register_user_duplicate_username(self, client):
        payload = self.generate_payload(username='user01', email='example@email.com')

        client.post(self.url, json=payload)
        payload = self.generate_payload(email='example2@email.com')
        response = client.post(self.url, json=payload)

        response_json = response.json
        assert response.status_code == 409
        assert not response_json.get('success')
        assert 'Username já registrado.' in response_json.get('message')

    def test_register_user_duplicate_email(self, client):
        payload = self.generate_payload(username='user01', email='example@email.com')

        client.post(self.url, json=payload)
        payload = self.generate_payload(username='user02', email='example@email.com')
        response = client.post(self.url, json=payload)

        response_json = response.json
        assert response.status_code == 409
        assert not response_json.get('success')
        assert 'Email já registrado.' in response_json.get('message')

    def test_register_user_invalid_email(self, client):
        payload = self.generate_payload(email='invalid_email')

        response = client.post(self.url, json=payload)

        assert response.status_code == 400
        assert not response.json.get('success')
        assert 'Email inválido.' in response.json.get('message')
    
    def test_register_user_invalid_password(self, client):
        payload = self.base_payload.copy()
        payload['password'] = 'weakpassword'

        response = client.post(self.url, json=payload)

        assert response.status_code == 400
        assert not response.json.get('success')
        assert 'Senha inválida.' in response.json.get('message')
    
    def test_register_user_underage(self, client):
        generate_young_birthdate = (date.today() - timedelta(days=randint(365, 365 * 13))).strftime('%Y-%m-%d')
        payload = self.generate_payload(username='user02',  email='example2@email.com')
        payload['birthdate'] = generate_young_birthdate

        response = client.post(self.url, json=payload)

        assert response.status_code == 403
        assert not response.json.get('success')
        assert 'Usuário não atinge a idade necessária para a utilização do app.' in response.json.get('message')

    def test_register_user_invalid_phone_number(self, client):
        payload = self.generate_payload(username='user03',  email='example3@email.com')
        payload['phone_number'] = '115262'

        response = client.post(self.url, json=payload)

        assert response.status_code == 400
        assert not response.json.get('success')
        assert 'Número de telefone inválido.' in response.json.get('message')

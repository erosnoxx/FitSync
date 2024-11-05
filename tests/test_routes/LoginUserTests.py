import pytest


@pytest.mark.controllers
@pytest.mark.login_resource
class LoginUserTests:
    def setup_class(self):
        self.url = '/api/v1/auth/users/login/'
        self.base_payload = {
            'username': 'user01',
            'password': 'Strongpassword123@'
        }

        self.register_url = '/api/v1/auth/users/register/'
        self.register_payload = {
            'username': 'user01',
            'email': 'example@email.com',
            'password': 'Strongpassword123@',
            'first_name': 'John',
            'last_name': 'Doe',
            'birthdate': '2000-01-01',
            'phone_number': '11996857412'
        }

        self.logout_url = '/api/v1/auth/users/logout/'

    def generate_payload(self, username=None, password=None):
        payload = self.base_payload.copy()
        if username is not None:
            payload['username'] = username
        if password is not None:
            payload['password'] = password
        return payload

    def test_login_user_success(self, client):
        client.post(self.register_url, json=self.register_payload)

        response = client.post(self.url, json=self.base_payload)

        response_json = response.json

        assert response.status_code == 200
        assert response_json.get('success')
        assert response_json.get('id')
        assert 'Usuário logado com sucesso.' in response_json.get('message')
    
    def test_login_invalid_username(self, client):
        payload = self.generate_payload(username='johndoe')

        response = client.post(self.url, json=payload)

        response_json = response.json
        assert response.status_code == 404
        assert not response_json.get('success')
        assert 'Nome de usuário inválido.' in response_json.get('message')

    def test_login_invalid_password(self, client):
        client.post(self.register_url, json=self.register_payload)

        payload = self.generate_payload(password='weakpassword')
        response = client.post(self.url, json=payload)

        response_json = response.json
        assert response.status_code == 400
        assert not response_json.get('success')
        assert 'Senha inválida.' in response_json.get('message')
    
    def test_login_incorrect_password(self, client):
        client.post(self.register_url, json=self.register_payload)

        payload = self.generate_payload(password='StrongPassword8@')
        response = client.post(self.url, json=payload)

        response_json = response.json
        assert response.status_code == 401
        assert not response_json.get('success')
        assert 'Senha incorreta.' in response_json.get('message')
    
    def test_logout_user_success(self, client):
        client.post(self.register_url, json=self.register_payload)
        response = client.delete(self.logout_url)

        assert response.status_code == 200
        assert response.json.get('success')
        assert 'Usuário deslogado com sucesso.' in response.json.get('message')
    
    def test_logout_fails_when_no_user_logged_in(self, client):
        client.post(self.register_url, json=self.register_payload)
        client.delete(self.logout_url)
        response = client.delete(self.logout_url)

        assert response.status_code == 401
        assert not response.json.get('success')
        assert 'Você precisa estar autenticado para acessar esse recurso.' in response.json.get('message')

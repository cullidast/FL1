import unittest
from flask import Flask
from app.auth.views import auth_bp

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.register_blueprint(auth_bp)

        self.client = self.app.test_client()

    def test_login_route(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        # Дополнительные проверки, например, наличие ожидаемого содержимого

    def test_protected_route_without_login(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 302)
        # Проверка перенаправления на страницу авторизации

    def test_protected_route_with_login(self):
        # Вход в систему перед доступом к защищенному маршруту
        with self.client:
            self.client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})

            response = self.client.get('/protected')
            self.assertEqual(response.status_code, 200)
            # Дополнительные проверки, например, наличие ожидаемого содержимого

    def test_some_function(self):
        from app import app
        # Ваш код, использующий объект app

if __name__ == '__main__':
    unittest.main()

import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

PYTHON_APP_URL_DEFAULT = 'http://python-app:5000' # Nombre de servicio y puerto interno
WIREMOCK_URL_DEFAULT = 'http://wiremock_service:8080' # Nombre de servicio y puerto interno

BASE_URL = os.environ.get('PYTHON_APP_URL', PYTHON_APP_URL_DEFAULT)
BASE_URL_MOCK = os.environ.get('WIREMOCK_URL', WIREMOCK_URL_DEFAULT)
DEFAULT_TIMEOUT = 10  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
        )

    def test_api_sqrt(self):
        url = f"{BASE_URL_MOCK}/calc/sqrt/64"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
